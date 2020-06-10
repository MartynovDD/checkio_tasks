"""
In a given text you need to sum the numbers. 
Only separated numbers should be counted. 
If a number is part of a word it shouldn't be counted.
The text consists from numbers, spaces and english letters
https://py.checkio.org/ru/mission/sum-numbers/
"""

import re


def sum_numbers(text):
    """
    Sums all separated digits in given string.
    Numbers that are part of the word are not counted.
    """
    split_text = text.split()
    numbers_list = []
    for i in split_text:
        # try:
        #     numbers_list.append(int(i))
        # except ValueError:
        #     pass
        if i.isdigit():
            numbers_list.append(int(i))
    if len(numbers_list) == 0:
        return 0
    return sum(numbers_list)


def sum_numbers_regex(text):
    """
    Does the same as 'sum_numbers()' funcs but using regex
    """
    numbers_list = re.findall(r"\b(\d+)\b", text)
    if len(numbers_list) == 0:
        return 0
    return sum(map(int, numbers_list))


def unified_sum_func(text):
    """
    Compares results of 'sum_numbers()' and 'sum_numbers_regex()' funcs
    and returns sum of numbers in text if both results are equal
    """
    assert sum_numbers(text) == sum_numbers_regex(text), "Results {} & {} are not equal".format(
        sum_numbers(text), sum_numbers_regex(text))
    return sum_numbers(text)


def check_sum_funcs(text, expected):
    assert sum_numbers(text) == sum_numbers_regex(text) == expected


if __name__ == "__main__":
    assert check_sum_funcs("", 0)  # Case 1
    assert check_sum_funcs("test", 0)  # Case 2
    assert check_sum_funcs("1", 1)  # Case 3
    assert check_sum_funcs("test123 5", 5)  # Case 4
    assert check_sum_funcs("421 1111", 1532)  # Case 5
    assert check_sum_funcs("123foo 1 bar100 3 4spam6 6 ", 10)  # Case 6
    assert check_sum_funcs("123\nbar45", 123)  # Case 6

