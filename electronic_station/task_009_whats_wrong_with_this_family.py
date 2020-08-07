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


def is_family(people: List[list]) -> bool:
    """
    Checks if given people are members of same family
    :param people: A list of people to analyze. Each man is represented by nested list of lists
    :return:
    """
    pass