import pytest
from electronic_station.task_005_ascending_list import is_ascending


def test_ascending():
    assert is_ascending([-5, 10, 99, 123456]), "Ascending items"


def test_descending():
    assert not is_ascending((9, 8, 7, 6, 5)), "Descending items"


def test_mixed():
    assert not is_ascending([4, 5, 6, 7, 3, 7, 9]), "Mixed items"


def test_equal():
    assert not is_ascending([0, 0, 0, 0]), "Equal items"


def test_empty_list():
    assert is_ascending([]), "Empty list"


def test_no_args():
    with pytest.raises(TypeError):
        is_ascending()


def test_incorrect_args():
    with pytest.raises(TypeError):
        is_ascending(3)


def test_iter():
    assert is_ascending(iter([1, 2]))