import pytest
from home.task_019_split_list import split_list


def test_even_length():
    assert split_list([1, 2, 3, 4]) == [[1, 2], [3, 4]], "Even length"


def test_odd_length():
    assert split_list([1, 2, 3]) == [[1, 2], [3]], "Odd length"


def test_long_odd_length():
    assert split_list([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 2, 3, 4, 5], [6, 7, 8, 9]], "Long odd length"


def test_empty_list():
    assert split_list([]) == [[], []], "Empty list"


def test_one_element():
    assert split_list([1]) == [[1], []], "One element"


def test_string():
    assert split_list("hello") == [["h", "e", "l"], ["l", "o"]], "A string"


def test_no_argument():
    with pytest.raises(TypeError):
        split_list()


def test_incorrect_argument():
    with pytest.raises(TypeError):
        split_list(123456)
