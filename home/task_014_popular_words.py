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
from utils.exception_catcher import exception_catcher


def popular_words(text: str, words: list) -> dict:
    """
    Using a list words, finds and returns dict with number of occurencies of each word in given text
    """
    split_data = text.lower().split()
    output = {}
    for char in words:
        output[char] = split_data.count(char)
    return output


if __name__ == "__main__":
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
    }, "i=4 was=3"
    assert popular_words("1 Hello hello hELLo", ["hello"]) == {"hello": 3}, "Multiple word cases"
    assert popular_words("", []) == {}, "Empty text and list"
    assert popular_words("", ["test"]) == {"test": 0}, "Empty text, list with one word"
    assert popular_words("test", []) == {}, "One word, empty list"
    assert exception_catcher(popular_words, ["Test", "text", "test", "spam"], ["test"]) == AttributeError, "Two lists"
    assert exception_catcher(popular_words) == TypeError, "Zero arguments"
    assert exception_catcher(popular_words, 343, 345) == AttributeError, "Incorrect arguments"