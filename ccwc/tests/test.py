import pytest
from src.main import ccwc
from . import get_fixture_path

@pytest.mark.parametrize(
    "filename, expected",
    [
        ("empty.txt", {'-c': 0, '-l': 0, '-w': 0, '-m': 0}),
        ("single-char.txt", {'-c': 1, '-l': 1, '-w': 1, '-m': 1}),
        ("multilines.txt", {'-c': 127, '-l': 3, '-w': 16, '-m': 127}),
        ("test.txt", {'-c': 342190, '-l': 7145, '-w': 58164, '-m': 332147}),
    ],
)
def test_ccwc(filename, expected):
    full_path = get_fixture_path(filename)
    assert ccwc(full_path) == expected