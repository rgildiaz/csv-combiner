import pandas as pd
import sys
import os
from typing import List
from pathlib import Path


def validate_paths(paths: List[Path], verbose: bool = False) -> None:
    '''
    Ensures the paths are valid and raises errors if not.

    Args:
        input (List[Path]) : the paths to the .csv files to be combined.
    Returns:
        None
    '''
    # Typer validates input type, no need to do it here

    # List validation
    if len(paths) < 2:
        sys.exit(
            f'Cannot combine less than 2 files. {len(paths)} file given.\n')

    # Path/file validation
    invalid_paths = []
    not_files = []
    for path in paths:
        if not os.path.exists(path):
            sys.stderr.write(f'Path "./{path}" does not exist.\n')
            invalid_paths.append(path)
        if not os.path.isfile(path):
            sys.stderr.write(f'Object at path "./{path}" is not a file.\n')
            not_files.append(path)

    # Exit with errors if any were found
    err_str = ""
    if invalid_paths:
        err_str += f"\t{len(invalid_paths)} invalid path(s) found."
    if not_files:
        err_str += f"\t{len(not_files)} non-file object(s) found."
    if err_str:
        sys.exit(f"\n{err_str}\n")

    if verbose:
        path_list = "\n\t".join([str(p) for p in paths])
        sys.stdout.write(f'\nPaths validated: \n\t{path_list}\n')


def read_file(path: Path) -> pd.DataFrame:
    '''
    Creates a DataFrame given a .csv at the path.

    Args:
        path (Path) : the path to the .csv file to be read.
    Returns:
        pd.DataFrame : the generated DataFrame. 
    '''
    try:
        df = pd.read_csv(path)
    except pd.errors.ParserError as e:
        sys.exit(f'File at path "{path}" cannot be parsed:\n\t{e}')
    except Exception as e:
        sys.exit(f'Error while reading file at path "{path}":\n\t{e}')

    df['filename'] = path.name

    return df


def write_csv(
    files: List[pd.DataFrame],
    remove_duplicate_rows: bool
) -> None:
    '''
    Writes DataFrames from a List to a single combined csv. Prints to stdout.

    Args:
        files (List[pd.DataFrame]) : the DataFrames to combine.
        outfile (Path): the location to write the new CSV to.
        remove_duplicate_rows (bool) : removes duplicate rows from generated CSV.
    '''
    df = pd.concat(files)

    if remove_duplicate_rows:
        df.drop_duplicates(inplace=True)

    sys.stdout.write(df.to_csv(index=False))
