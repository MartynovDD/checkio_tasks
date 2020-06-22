import pytest
from home.task_014_popular_words import popular_words
from utils.exception_catcher import exception_catcher


def test_long_string():
    assert popular_words("""
        When I was One
        I had just begun
        When I was Two
        I was nearly new
        """, ["i", "was", "three", "near"]) == {
        "i": 4,
        "was": 3,
        "three": 0,
        "near": 0
    }, "Long string"


def test_multiple_word_cases():
    assert popular_words("1 Hello hello hELLo", ["hello"]) == {"hello": 3}, "Multiple word cases"


def test_empty_text_and_list():
    assert popular_words("", []) == {}, "Empty text and list"


def test_empty_text_one_word_list():
    assert popular_words("", ["test"]) == {"test": 0}, "Empty text, list with one word"


def test_word_and_empty_list():
    assert popular_words("test", []) == {}, "One word, empty list"


def test_two_lists():
    assert exception_catcher(popular_words, ["Test", "text", "test", "spam"], ["test"]) == AttributeError, "Two lists"


def test_zero_arguments():
    assert exception_catcher(popular_words) == TypeError, "Zero arguments"


def test_incorrect_arguments():
    assert exception_catcher(popular_words, 343, 345) == AttributeError, "Incorrect arguments"
