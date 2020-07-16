import pytest
from electronic_station.task_001_words_order import words_order


def test_hello_world():
    assert words_order("hello spam world eggs", ["hello", "world"]), "Hello world"


def test_hello_world_reversed():
    assert not words_order("hello spam world eggs", ["world", "hello"]), "Reversed words"


def test_one_word():
    assert words_order("hello spam world eggs", ["world"]), "One word"


def test_different_cases():
    assert not words_order("hello Spam world eggs", ["spam", "eggs"]), "Different word cases"


def test_word_parts():
    assert not words_order("hello spam world eggs", ["sp", "am"]), "Word parts"


def test_empty_text():
    assert not words_order("", ["spam", "eggs"]), "Empty word"


def test_empty_words():
    assert not words_order("hello world", []), "Empty list"


def test_empty_text_and_words():
    assert not words_order("", []), "Empty text and words"


def test_repeated_words():
    assert words_order("hello spam eggs world world hello", ["hello", "world"]), "Repeated words"


def test_no_args():
    with pytest.raises(TypeError):
        words_order()


def test_incorrect_args():
    with pytest.raises(TypeError):
        words_order(43242, 3)
