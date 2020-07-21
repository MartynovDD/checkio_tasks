import pytest
from electronic_station.task_001_words_order import words_order
from hypothesis import given, assume, settings, Verbosity, strategies as st


@given(s1=st.text(alphabet=st.characters(blacklist_categories=("Cs", "Cc", "Zs")), min_size=1),
       s2=st.text(alphabet=st.characters(blacklist_categories=("Cs", "Cc", "Zs")), min_size=1))
@settings(max_examples=1000, verbosity=Verbosity.verbose)
def test_hello_world(s1, s2):
    assume(s1 != s2)
    assert words_order("{0} spam {1} eggs".format(s1, s2), [s1, s2]), "Hello world"


@given(s1=st.text(), s2=st.text())
@settings(max_examples=1000, verbosity=Verbosity.verbose)
def test_hello_world_reversed(s1, s2):
    assert not words_order("{0} spam {1} eggs".format(s1, s2), [s2, s1]), "Reversed words"


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
