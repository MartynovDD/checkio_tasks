"""
 Let's teach the Robots to distinguish words and numbers.

 You are given a string with words and numbers separated by whitespaces (one space).
 The words contains only letters.
 You should check if the string contains three words in succession.
 For example, the string "start 5 one two three 7 end" contains three words in succession.
 https://py.checkio.org/ru/mission/even-last/
"""


def words_counter(words):
    """
    Count subsequent words in a string,
    return True if there are three words in succession,
    otherwise return False
    """
    count = 0
    for w in words.split():
        if w.isalpha():
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False


if __name__ == '__main__':
    assert words_counter("Hello World hello") == True, "Case 1"
    assert words_counter("He is 123 man") == False, "Case 2"
    assert words_counter("1 2 3 4") == False, "Case 3"
    assert words_counter("bla bla bla bla") == True, "Case 4"
    assert words_counter("Hi") == False, "Case 5"
    assert words_counter("qwe fds 32 khh wwewe 123 uiu 8794 ") == False, "Case 6"
    assert words_counter("0 qwerty 99999999999 asdfg 2") == False, "Case 7"
    assert words_counter("0 qwerty a asdfg 2 ") == True, "Case 8"
    assert words_counter("1231 321 3123 12312 3231 321 312 3123 1231 ") == False, "Case 9"
