"""
 One of the robots is charged with a simple task: to join a sequence of strings
 into one sentence to produce instructions on how to get around the ship.
 But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.

 You are given a sequence of strings.
 You should join these strings into a chunk of text where the initial strings are separated by commas.
 As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left",
 even if it's a part of another word.
 All strings are given in lowercase.
 https://py.checkio.org/ru/mission/right-to-left/
"""


def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    joined_phrases = ','.join(phrases)
    return joined_phrases.replace("right", "left")


if __name__ == '__main__':
    assert left_join(("right", "right")) == "left,left", "Case 1"
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "Case 2"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Case 3"
    assert left_join(("brightness wright",)) == "bleftness wleft", "Case 4"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Case 5"
    assert left_join(("r", "i", "g", "h", "t",)) == "r,i,g,h,t", "Case 6"
