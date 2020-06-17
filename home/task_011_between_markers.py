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


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    if begin in text:
        start = text.find(begin) + len(begin)
    else:
        start = 0
    if end in text:
        finish = text.find(end)
    else:
        finish = len(text)

    return text[start:finish]


if __name__ == "__main__":
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'