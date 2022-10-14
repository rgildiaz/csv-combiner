from csv_combiner import write_csv
import pytest
import pandas as pd
import csv
from fixtures.fixtures import *


@pytest.fixture
def real_dfs(real_paths):
    return make_dfs(real_paths)


@pytest.fixture
def large_csv_dfs(large_csv_paths):
    return make_dfs(large_csv_paths)


@pytest.fixture
def dif_columns_dfs(dif_columns_paths):
    return make_dfs(dif_columns_paths)


@pytest.fixture
def small_dfs(real_paths_small):
    return make_dfs(real_paths_small)


def test_valid_dfs(real_dfs):
    write_csv(real_dfs)


def test_small_files(small_dfs):
    # testing using pd.read_csv() and .to_csv() since that is how the csvs are combined
    csv_str = pd.read_csv("./tests/fixtures/small/small_combined.csv").to_csv(index=False)
    assert write_csv(small_dfs) == csv_str


def _test_large_file(large_csv_dfs):
    write_csv(large_csv_dfs)


def test_dif_columns(dif_columns_dfs):
    write_csv(dif_columns_dfs)


def make_dfs(paths):
    dfs = []
    for path in paths:
        df = pd.read_csv(path)
        df['filename'] = path.name
        dfs.append(df)
    return dfs
