from csv_combiner import validate_paths
from pathlib import Path
import pytest
from fixtures.fixtures import *


def test_is_list():
    with pytest.raises(SystemExit) as e:
        validate_paths(Path("./tests"))
        assert e.type == SystemExit
        assert e.value.code == 42


def test_at_least_two_paths(real_paths):
    with pytest.raises(SystemExit) as e:
        path = real_paths[0]
        validate_paths([path])
        assert e.type == SystemExit
        assert e.value.code == 42


def test_no_paths():
    with pytest.raises(SystemExit) as e:
        validate_paths([])
        assert e.type == SystemExit
        assert e.value.code == 42


def test_real_paths(real_paths):
    assert validate_paths(real_paths) is True


def test_return_type(real_paths):
    assert isinstance(validate_paths(real_paths), bool)


def test_nonpath_list():
    with pytest.raises(SystemExit) as e:
        validate_paths([object, TypeError, list])
        assert e.type == SystemExit
        assert e.value.code == 42
