import pytest
from home.task_012_most_wanted_letter import most_wanted_letter
from utils.exception_catcher import exception_catcher


def test_hello():
    assert most_wanted_letter("Hello World!") == "l", "Hello test"


def test_letters_only_once():
    assert most_wanted_letter("One") == "e", "All letter only once."


def test_lowercase():
    assert most_wanted_letter("Oops!") == "o", "Lowercase test"


def test_first_letter():
    assert most_wanted_letter("abe") == "a", "The first."


def test_long_words():
    assert most_wanted_letter("a" * 9000 + "b" * 1000) == "a", "Long."


def test_alphabet_backwards():
    assert most_wanted_letter("ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba") == "a", "Alphabet backwards"


def test_letters_with_minuses():
    assert most_wanted_letter("i-d-d-q-d") == "d", "Letters with minuses"


def test_spaced_letter():
    assert most_wanted_letter("      d       ") == "d", "Spaced letter"


def test_letter_with_numbers():
    assert most_wanted_letter("12345,12345,12345 S 12345,12345") == "s", "Letter with numbers"


def test_empty_string():
    assert most_wanted_letter("") == "", "Empty string"


def test_one_space():
    assert most_wanted_letter(" ") == "", "One space"


def test_zero_arguments():
    assert exception_catcher(most_wanted_letter) == TypeError, "Zero arguments"


def test_incorrect_argument():
    assert exception_catcher(most_wanted_letter, 123456) == AttributeError
