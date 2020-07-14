"""
You are given a string where you have to find its first word.
When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
https://py.checkio.org/ru/mission/three-words/
"""
import typing


def first_word(text: typing.Any) -> str:
    """
        Returns the first word in a given text.
    """
    if type(text) != str or not text:
        return "invalid value"
    cleaned_text = text.replace('.', ' ').replace(',', ' ').strip()
    words = cleaned_text.split()
    return words[0]


if __name__ == "__main__":
    assert first_word("Hello world") == "Hello", "Case 1"
    assert first_word(" a word ") == "a", "Case 2"
    assert first_word("don't touch it") == "don't", "Case 3"
    assert first_word("greetings, friends") == "greetings", "Case 4"
    assert first_word("Hello.World") == "Hello", "Case 5"
    assert first_word("hi") == "hi", "Case 6"
    assert first_word("") == "invalid value", "Case 7"
    assert first_word(1) == "invalid value", "Case 8"


