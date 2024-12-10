from pathlib import Path

import pytest

from src.ccwc import count_bytes, count_lines, count_words


@pytest.fixture
def fp():
    base_path = Path(__file__)
    resources = base_path.absolute().parent / "resources"
    test_text = resources / "test.txt"
    with open(test_text, "rb") as f:
        yield f


def test_count_bytes(fp):
    expected = 342190
    actual = count_bytes(fp)
    assert actual == expected


def test_count_lines(fp):
    expected = 7145
    actual = count_lines(fp)
    assert actual == expected


def test_count_words(fp):
    expected = 58164
    actual = count_words(fp)
    assert actual == expected
