"""
You have a list of family ties between father and son.
Each element on this list has two elements.
The first is the father's name, the second is the son's name.
All names in the family are unique. Check if the family tree is correct.
There are no strangers in the family tree. All connections in the family are natural.

Input: list of lists. Each element has two strings. The list has at least one element

Output: bool. Is the family tree correct.
"""
from utils.check_type import check_type
from typing import List


def is_family(people: List[List[str]]) -> bool:
    """
    Checks if given people are members of same family
    :param people: A list of people to analyze. Each person is represented by nested list of lists
    :return:
    """
    pass


def validate_people(people: List[List[str]]):
    """
    Validates type of given list of people
    :param people: List of lists of strings, representing fathers and sons
    :return: None if list is valid, raises TypeError otherwise
    """
    check_type(list, people)
    for pair in people:
        check_type(list, pair)
        for name in pair:
            check_type(str, name)


if __name__ == "__main__":
    validate_people([["Logan", "Mike"], ["Logan", "Alex"]])
    validate_people([[1, 2], [3.4, 4.5]])