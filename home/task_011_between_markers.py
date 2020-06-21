"""
You are given a string and two markers (the initial and final).
You have to find a substring enclosed between these two markers. But there are a few important conditions:

 The initial and final markers are always different.
 If there is no initial marker, then the first character should be considered the beginning of a string.
 If there is no final marker, then the last character should be considered the ending of a string.
 If the initial and final markers are missing then simply return the whole string.
 If the final marker comes before the initial marker, then return an empty string.
 https://py.checkio.org/en/mission/between-markers/
"""


class PreConditionException(Exception):
    pass


def between_markers(text: str, begin: str, end: str) -> str:
    """
        Returns substring between two given markers
    """
    try:
        if begin in text:
            start = text.find(begin) + len(begin)
        else:
            start = 0
        if end in text:
            finish = text.find(end)
        else:
            finish = len(text)
        return text[start:finish]
    except TypeError:
        return "error"


if __name__ == "__main__":
    assert between_markers("What is >apple<", ">", "<") == "apple", "One word"
    assert between_markers("<body<h1>Foo bar</h1></body>",
                           "<h1>", "</h1>") == "Foo bar", "HTML tags"
    assert between_markers("Spam> hi", "<", ">") == "Spam", "Only ending marker"
    assert between_markers("Hello [b]world", "[b]", "[/b]") == "world", "Only opening marker"
    assert between_markers("print me", "[b]", "[/b]") == "print me", "No markers at all"
    assert between_markers("No <hi>", ">", "<") == "", "Wrong direction"
    # assert between_markers("No <hi>", "", "") == "No <hi>", "Wrong direction"
    assert between_markers("(123)", "(", ")") == "123", "Numbers in bracers"
    assert between_markers("", "{", "}") == "", "Empty string"
    assert between_markers("{error}", "{", "}") == "error", "Empty string"
    assert between_markers(123, 1, 3) == "error", "Incorrect arguments"
    assert between_markers("bla bla bla</b> text<b> qwerty", "<b>", "</b>") == ""
    # assert between_markers(list(range(10)), 1, 3) == "error"
