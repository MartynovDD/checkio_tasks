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


def is_family(tree: List[List[str]]) -> bool:
    """
    Checks if given tree are members of same family
    :param tree: A list of tree to analyze. Each person is represented by nested list of lists
    :return:
    """
    validate_tree(tree)
    if family_has_equal_names(tree):
        return False

    family = set(tree[0])
    for father, son in tree[1:]:
        if father in family and son not in family:
            family.add(son)
        else:
            return False
    return True


def validate_tree(tree: List[List[str]]) -> None:
    """
    Validates type of given list of tree
    :param tree: List of lists of strings, representing fathers and sons
    :return: None if list is valid, raises TypeError otherwise
    """
    check_contents_of_tree(tree)
    check_type(list, tree)
    for pair in tree:
        check_type(list, pair)
        for name in pair:
            check_type(str, name)


def check_contents_of_tree(tree: List[List[str]]) -> None:
    """
    Checks that given family tree is not empty or doesn't contain empty sublists
    :param tree: List of lists of strings, representing fathers and sons
    :return: None if list is valid, raises ValueError otherwise
    """
    if not tree:
        raise ValueError("Given family tree is empty")

    for pair in tree:
        if not pair:
            raise ValueError("Given tree contains empty family")


def family_has_equal_names(tree: List[List[str]]) -> bool:
    """
    Checks if family in tree has equal names of father and son
    :param tree: List of lists of strings, representing fathers and sons
    :return:
    """
    for father, son in tree:
        if father == son:
            return True

    return False
