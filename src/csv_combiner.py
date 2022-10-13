import typer
from typing import List
from pathlib import Path
import pandas as pd
import sys
import os


app = typer.Typer()


@app.command()
def main(
    files: List[Path] = typer.Argument(..., help="Files to be combined."),
    drop_duplicate_rows: bool = typer.Option(
        False, "--drop-duplicates", "-d", help="Drop duplicate rows in output.")
):
    """
    Combine multiple .csv's into a single file!
    """
    validate_paths(files)

    csvs = []
    for f in files:
        csv = read_file(f)
        csvs.append(csv)

    write_csv(csvs, drop_duplicate_rows)


def validate_paths(paths: List[Path]) -> bool:
    '''
    Ensures the paths are valid and raises errors if not.

    Args:
        input (List[Path]) : the paths to the .csv files to be combined.
    Returns:
        bool : whether or not the paths are valid.
    '''
    # List validation
    if not isinstance(paths, List):
        sys.exit(f'Input must be of type List. Type {type(paths)} given.\n')
    if len(paths) < 2:
        sys.exit(
            f'Cannot combine less than 2 files. {len(paths)} file given.\n')

    # Path/file validation
    invalid_paths = []
    not_files = []
    for path in paths:
        try:
            if not os.path.exists(path):
                sys.stderr.write(f'Path "./{path}" does not exist.\n')
                invalid_paths.append(path)
            elif not os.path.isfile(path):
                sys.stderr.write(f'Object at path "./{path}" is not a file.\n')
                not_files.append(path)
        except Exception:
            sys.stderr.write(
                f'Path "./{path}" must be of type Path. Type {type(path)} given.\n')
            invalid_paths.append(path)

    # Exit with errors if any were found
    err_str = ""
    if invalid_paths:
        err_str += f"\t{len(invalid_paths)} invalid path(s) found."
    if not_files:
        err_str += f"\t{len(not_files)} non-file object(s) found."
    if err_str:
        sys.exit(f"\n{err_str}\n")

    return True


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
    remove_duplicate_rows: bool = False
) -> None:
    '''
    Writes DataFrames from a List to a single combined csv. Prints to stdout.

    Args:
        files (List[pd.DataFrame]) : the DataFrames to combine.
        remove_duplicate_rows (bool) : removes duplicate rows from generated CSV.
    Returns:
        None
    '''
    if not isinstance(files, List):
        sys.exit(
            f"Argument 'files' must be of type List. Type {type(files)} given.\n")
    if not len(files) > 1:
        sys.exit(
            f"Argument 'files' must be of length 2 or greater. Length {len(files)} given.\n")
    for i, f in enumerate(files):
        if not isinstance(f, pd.DataFrame):
            sys.exit(
                f"Argument 'files' must contain only DataFrames. Object {repr(f)} found at index {i}.\n")

    df = pd.concat(files)

    if remove_duplicate_rows:
        df.drop_duplicates(inplace=True)

    csv = df.to_csv(index=False)
    sys.stdout.write(csv)


if __name__ == "__main__":
    app()
