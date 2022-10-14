from csv_combiner import read_file
import pytest
from pandas import DataFrame
from fixtures.fixtures import *


def test_return_type(real_paths):
    path = real_paths[0]
    assert isinstance(read_file(path), DataFrame)


def test_nonpath_input(real_paths):
    with pytest.raises(SystemExit) as e:
        # try to read list
        read_file(real_paths)
        assert e.type == SystemExit
        assert e.value.code == 42

def _test_large_files(large_csv_paths):
    for i in large_csv_paths:
        read_file(i)