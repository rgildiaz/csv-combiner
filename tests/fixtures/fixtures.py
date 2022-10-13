from pathlib import Path
import pytest

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