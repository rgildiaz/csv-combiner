from pathlib import Path
from typing import List
import csv
import random
import os
import pytest
import pandas as pd

LARGE_CSV_COUNT = 2
LARGE_CSV_DIR = './tests/fixtures/large'


@pytest.fixture
def fake_paths():
    paths = [
        "./this/is/a/fake/path.csv",
        "./another/fake/path.csv",
        "./one/more/fake/path.csv",
    ]
    return [Path(i) for i in paths]


@pytest.fixture
def real_paths():
    paths = [
        "./tests/fixtures/clothing.csv",
        "./tests/fixtures/accessories.csv",
        "./tests/fixtures/household_cleaners.csv"
    ]
    return [Path(i) for i in paths]


@pytest.fixture
def dif_columns_paths():
    paths = [
        Path("./tests/fixtures/clothing.csv")
    ]
    path_str = "./tests/fixtures/dif_columns.csv"
    if not os.path.exists(path_str):
        path = generate_csv(
            path=Path("./tests/fixtures/"),
            fname="dif_columns.csv",
            rows=20
        )
    else:
        path = Path(path_str)

    paths.append(path)

    return paths


@pytest.fixture
def large_csv_paths() -> List[Path]:
    '''Returns a list of paths to two .csvs that are over 2GB.'''
    # Create dir if it doesn't already exist
    path = Path(LARGE_CSV_DIR)
    if not os.path.exists(path):
        os.mkdir(path)

    # Return a list of large CSVs that already exist,
    # or create new CSVs if they don't.
    dir_list = os.listdir(path)
    large_files_list = [
        path / i for i in dir_list if
        os.path.getsize(f'{str(path)}/{i}') > 2 * (10**9)
    ]
    num_large_files = len(large_files_list)

    if (len(dir_list) >= LARGE_CSV_COUNT) and \
            (num_large_files >= LARGE_CSV_COUNT):
        return [i for i in large_files_list[:LARGE_CSV_COUNT]]
    else:
        for fd in dir_list:
            os.remove(path / fd)

        generated_csvs = []
        for i in range(LARGE_CSV_COUNT - num_large_files):
            csv = generate_csv(
                path=path,
                fname=f"lg_test{i + num_large_files}.csv",
                rows=2 * (10**8)
            )
            generated_csvs.append(csv)
        return generated_csvs


def generate_csv(
    path: Path,
    fname: str,
    rows: int
) -> Path:
    '''Generates a CSV at the path named fname with designated number of rows'''
    with open(f'{str(path)}/{fname}', 'x', newline='') as fd:
        fieldnames = ['email_hash', 'dummy_hash']
        writer = csv.DictWriter(fd, fieldnames=fieldnames)

        writer.writeheader()
        # write 12 characters per row for 200,000,000 rows >= 2.4 GB
        for _ in range(rows):
            writer.writerow({
                'email_hash': random.randint(10**5, 999999),
                'dummy_hash': random.randint(10**5, 999999)
            })
    return Path(f'{str(path)}/{fname}')
