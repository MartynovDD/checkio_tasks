"""
In a given string you should reverse every word, but the words should stay in their places.
https://py.checkio.org/ru/mission/backward-each-word/
"""


def word_reverse(text: str) -> str:
    try:
        for word in text.split():
            text = text.replace(word, word[::-1]) if word.isalpha() else text
    except AttributeError:
        return "error"
    return text


if __name__ == "__main__":
    assert word_reverse("") == "", "Empty string"
    assert word_reverse("hello") == "olleh", "One word"
    assert word_reverse("test string") == "tset gnirts", "Two words"
    assert word_reverse("abc abc a b c") == "cba cba a b c", "Words and letters"
    assert word_reverse("123 demo 4") == "123 omed 4", "Word between numbers"
    assert word_reverse("1337 696") == "1337 696", "Text contains only numbers"
    assert word_reverse("1337  696  ") == "1337  696  ", "Text contains only numbers"
    assert word_reverse("&&*%test") == "&&*%test", "Symbols + word"
    assert word_reverse(343) == "error", "Only strings are allowed"
    assert word_reverse("error") == "rorre", "Error"
    assert word_reverse("rorre") == "error", "Error backwards"
    assert word_reverse("rorre error") == "error rorre", "Error backwards"

