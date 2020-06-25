"""
In this mission your task is to determine the popularity of certain words in the text.
At the input of your function are given 2 arguments:
the text and the array of words the popularity of which you need to determine.

When solving this task pay attention to the following points:
 The words should be sought in all registers.
  This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
 The search words are always indicated in the lowercase.
 If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
"""


def popular_words(text: str, words: list) -> dict:
    """
    Finds and returns dict with number of occurencies of each word in given text
    :param text: str
    :param words: list
    :return: dict
    """
    split_data = text.lower().split()
    output = {}
    for char in words:
        output[char] = split_data.count(char)
    return output

