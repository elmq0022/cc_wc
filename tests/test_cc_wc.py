from pathlib import Path

import pytest

from src.cc_wc.cc_wc import count


@pytest.fixture
def fp():
    base_path = Path(__file__)
    resources = base_path.absolute().parent / "resources"
    test_text = resources / "test.txt"
    with open(test_text, "rb") as f:
        yield f


def test_count(fp):
    expected_lines = 7145
    expected_words = 58164
    expected_chars = 339292
    expected_bytes = 342190
    expected = (expected_lines, expected_words, expected_chars, expected_bytes)

    actual = count(fp)

    assert actual == expected
