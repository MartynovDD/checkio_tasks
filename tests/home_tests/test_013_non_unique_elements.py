import pytest
from home.task_013_non_unique_elements import non_unique_elements
from utils.exception_catcher import exception_catcher


def test_only_unique_elements():
    assert non_unique_elements([1, 2, 3, 4, 5]) == [], "Only unique elements"


def test_only_non_unique_elements():
    assert non_unique_elements([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "Only non-unique elements"


def test_one_unique_element():
    assert non_unique_elements([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "One unique element"


def test_words():
    assert non_unique_elements(["hello", "hello", "world"]) == ["hello", "hello"], "Words"


def test_floats():
    assert non_unique_elements([1.1 + 2.2, 3.3]) == [], "Floats"


def test_empty_list():
    assert non_unique_elements([]) == [], "Empty list"


def test_dictionary():
    assert non_unique_elements({"first": 1, "second": 1, "third": 3}) == [1, 1], "Dictionary"


def test_string():
    assert non_unique_elements("aaaagggrty") == ["a", "a", "a", "a", "g", "g", "g"], "A string"


def test_empty_string():
    assert non_unique_elements("") == [], "Empty string"


def test_list_with_empty_strings():
    assert non_unique_elements(["", "", "", "a"]) == ["", "", ""], "List with empty strings"


def test_zero_arguments():
    assert exception_catcher(non_unique_elements) == TypeError, "No arguments"


def test_incorrect_argument():
    assert exception_catcher(non_unique_elements, 53556) == TypeError, "Incorrect argument"
