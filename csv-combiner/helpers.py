import csv
import sys
import os
from typing import List
from pathlib import Path


def validate_paths(paths: List[Path]) -> None:
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
        sys.exit(f'Cannot combine less than 2 files. {len(paths)} file given.\n')

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
        err_str += f"\n{len(invalid_paths)} invalid path(s) found."
    if not_files:
        err_str += f"\n{len(not_files)} non-file object(s) found."
    if err_str:
        sys.exit(f"\n{err_str}\n")


def read_file(path: Path) -> csv.DictReader:
    '''
    Creates a csv reader object given a path to a .csv file. Exits with errors if file at path is not a CSV or if it cannot be opened.

    Args:
        path (Path) : the path to the .csv file to be read.
    Returns:
        csv.DictReader : the generated csv reader. 
    '''
    try:
        with open(path, newline="") as fd:
            try:
                reader = csv.reader(fd)
            except Exception:
                sys.exit(f'File at path "{str(path)}" is not .csv.')
    except Exception:
        sys.exit(f'File at path "{str(path)}" cannot be opened.')

    return reader


def write_csv(
    files: List[csv.DictReader],
    remove_duplicate_rows: bool = False
) -> None:
    '''
    Writes .csv files from a List to a single combined file.

    Args:
        files (List[csv.DictReader]) : the files to be written.
        remove_duplicate_rows (bool) : removes duplicate rows from generated CSV. Default value is False.
    Returns:
        csv.DictReader : the generated csv reader. 
    '''


if __name__ == "__main__":
    pass
