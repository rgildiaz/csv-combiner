from xmlrpc.client import Boolean
import typer
from typing import List
from pathlib import Path
from helpers import *


app = typer.Typer()


@app.command()
def main(
    files: List[Path] = typer.Argument(..., help="Files to be combined."),
    drop_duplicate_rows: bool = typer.Option(
        False, "--drop-duplicates", "-d", help="Drop duplicate rows in output."),
    verbose: bool = typer.Option(False, "--verbose", "-v")
):
    """
    Combine multiple .csv's into a single file!
    """
    validate_paths(files, verbose)

    csvs = []
    for f in files:
        csv = read_file(f)
        csvs.append(csv)

    write_csv(csvs, drop_duplicate_rows)


if __name__ == "__main__":
    app()
