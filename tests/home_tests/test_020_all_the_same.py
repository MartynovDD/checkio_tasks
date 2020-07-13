import pytest
from home.task_020_all_the_same import all_the_same


def test_not_equal():
    assert all_the_same([1, 2, 3]) is False, "Not equal"


def test_all_equal():
    assert all_the_same([1, 1, 1]) is True, "All equal"


def test_half_equal():
    assert all_the_same([1, 2, 1, 2, 1, 2]) is False, "Half equal, half not equal"


def test_one_not_equal():
    assert all_the_same([3, 3, 3, 3, 4]) is False, "One element is not equal to others"


def test_one_element():
    assert all_the_same([1]) is True, "One element"


def test_empty_list():
    assert all_the_same([]) is True, "Empty list"


def test_letters():
    assert all_the_same(["a", "a", "a", "a", "a"]) is True, "Equal letters"


def test_floats():
    assert all_the_same([2.22, 1.11 + 1.11, 2.22]) is True, "Floats"


def test_string():
    with pytest.raises(TypeError):
        all_the_same("BBBBBBBB")


def test_no_arguments():
    with pytest.raises(TypeError):
        all_the_same()


def test_incorrect_argument():
    with pytest.raises(TypeError):
        all_the_same(324234)
