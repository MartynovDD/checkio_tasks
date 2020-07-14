import pytest
from home.task_015_second_index import second_index
from utils.exception_catcher import exception_catcher


def test_one_word():
    assert second_index("sims", "s") == 3, "One word"


def test_two_words():
    assert second_index("find the river", "e") == 12, "Two words"


def test_word_with_space():
    assert second_index("hi ", " ") is None, "Word with space"


def test_two_spaces():
    assert second_index(" hi ", " ") == 3, "Two spaces"


def test_empty_string():
    assert second_index("", "") is None, "Empty string"


def test_empty_symbol():
    assert second_index("hello world", "") == 1, "Empty symbol"


def test_no_arguments():
    with pytest.raises(TypeError):
        second_index()


def test_one_argument():
    with pytest.raises(TypeError):
        second_index("hello")


def test_incorrect_arguments():
    with pytest.raises(AttributeError):
        second_index(314159265, 1)
