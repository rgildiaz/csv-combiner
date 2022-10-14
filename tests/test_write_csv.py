from csv_combiner import write_csv
import pytest
import pandas as pd
from fixtures.fixtures import *


@pytest.fixture
def real_dfs(real_paths):
    dfs = []
    for path in real_paths:
        df = pd.read_csv(path)
        df['filename'] = path.name
        dfs.append(df)
    return dfs

@pytest.fixture
def large_csv_dfs(large_csv_paths):
    dfs = []
    for path in large_csv_paths:
        df = pd.read_csv(path)
        df['filename'] = path.name
        dfs.append(df)
    return dfs

def test_valid_dfs(real_dfs):
    write_csv(real_dfs)

def test_large_file(large_csv_dfs):
    write_csv(large_csv_dfs)