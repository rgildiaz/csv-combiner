import typer
from typing import List
from pathlib import Path
from helpers import *


app = typer.Typer(rich_markup_mode=None)


@app.command()
def main(
    files: List[Path] = typer.Argument(..., help="Files to be combined."),
    remove_duplicate_rows: bool = False,
    verbose: bool = False
):
    """
    Combine multiple .csv's into a single file!
    """
    validate_paths(files)

    csvs = []
    for f in files:
        csv = read_file(f)
        csvs.append(csv)
    
    write_csv(csvs)


if __name__ == "__main__":
    app()
