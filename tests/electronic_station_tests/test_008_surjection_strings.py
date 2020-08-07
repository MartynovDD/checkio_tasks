import pytest
from electronic_station.task_008_surjection_strings import are_isometric


def test_isometric_strings():
    assert are_isometric("add", "egg"), "Isometric strings"


def test_non_isometric_strings():
    assert not are_isometric("foo", "bar"), "Non isometric strings"


def test_different_length():
    assert not are_isometric("spam", "egg"), "Different length of two strings"


def test_equal_strings():
    assert are_isometric("demo", "demo"), "Equal strings"


def test_empty_strings():
    assert are_isometric("", ""), "Empty strings"


def test_empty_values():
    with pytest.raises(TypeError):
        are_isometric()


def test_incorrect_values():
    with pytest.raises(TypeError):
        are_isometric(132, ("foo", "bar"))