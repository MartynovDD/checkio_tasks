"""
In a given string you should reverse every word, but the words should stay in their places.
https://py.checkio.org/ru/mission/backward-each-word/
"""


def word_reverse(text: str) -> str:
    for word in text.split():
        text = text.replace(word, word[::-1])
    return text


if __name__ == "__main__":
    assert word_reverse("") == "", "Case 1"
    assert word_reverse("hello") == "olleh", "Case 2"
    assert word_reverse("test string") == "tset gnirts", "Case 3"
    assert word_reverse("abc abc a b c") == "cba cba a b c", "Case 4"
    assert word_reverse("test  test") == "tset  tset", "Case 5"
