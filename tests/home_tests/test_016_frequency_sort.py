import pytest
from home.task_016_frequency_sort import frequency_sort
from utils.exception_catcher import exception_catcher


def test_words_list():
    assert frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex'], "Words list"


# @pytest.mark.skip
def test_numbers_list():
    # TODO Investigate
    assert frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2], "Numbers list"


def test_unique_items():
    assert frequency_sort([17, 99, 42]) == [17, 99, 42], "Unique items"


def test_empty_list():
    assert frequency_sort([]) == [], "Empty list"


def test_one_item():
    assert frequency_sort([1]) == [1], "One item"


def test_empty_strings():
    assert frequency_sort(["", "", "a", "", ""]) == ["", "", "", "", "a"], "Letter between empty strings"


def test_string():
    assert frequency_sort("hello") == ["l", "l", "h", "e", "o"], "One string"


def test_no_arguments():
    assert exception_catcher(frequency_sort) == TypeError, "No arguments"


def test_incorrect_argument():
    assert exception_catcher(frequency_sort, 4.4) == TypeError, "Incorrect argument"
