"""
In a given string you should reverse every word, but the words should stay in their places.
https://py.checkio.org/ru/mission/backward-each-word/
"""


def word_reverse(text):
    text_array = [list(w) for w in text.split()]
    for l in text_array:
        l.reverse()
    result_list = ["".join(lists) + " " for lists in text_array]
    result_text = "".join(result_list).strip()
    return result_text


if __name__ == "__main__":
    assert word_reverse("") == "", "Case 1"
    assert word_reverse("hello") == "olleh", "Case 2"
    assert word_reverse("test string") == "tset gnirts", "Case 3"
    assert word_reverse("abc abc a b c") == "cba cba a b c", "Case 4"
