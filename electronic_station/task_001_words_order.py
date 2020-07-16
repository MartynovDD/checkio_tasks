"""
You have a text and a list of words.
You need to check if the words in a list appear in the same order as in the given text.

Cases you should expect while solving this challenge:

    a word from the list is not in the text - your function should return False;
    any word can appear more than once in a text - use only the first one;
    two words in the given list are the same - your function should return False;
    the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
    the text includes only English letters and spaces.
https://py.checkio.org/ru/mission/words-order/
"""
from utils.check_type import check_type


def words_order(text: str, words: list) -> bool:
    """
    Checks if words in list appear in same order as in text
    :param text: str text to analyze
    :param words: list of words to search in text
    :return: True if order same or len(words) == 1, False otherwise
    """
    check_type(str, text)
    check_type(list, words)

    if not text or not len(words):
        return False

    return list(dict.fromkeys([word for word in text.split() if word in words])) == words
