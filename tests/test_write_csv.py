from csv_combiner import write_csv
import pytest
import pandas as pd
from fixtures.fixtures import *


@pytest.fixture
def real_dataframes(real_paths):
    dfs = []
    for path in real_paths:
        df = pd.read_csv(path)
        df['filename'] = path.name
        dfs.append(df)
    return dfs

def test_valid_dfs(real_dataframes):
    write_csv(real_dataframes)