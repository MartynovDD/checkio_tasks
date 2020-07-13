"""
In this mission you should check if all elements in the given list are equal.
https://py.checkio.org/en/mission/all-the-same/
"""
from utils.type_checker import type_checker


def all_the_same(items: list) -> bool:
    """
    Checks if all items in list are same
    :param items: a list of items to compare
    :return: True if all items are same, False if not
    """
    type_checker(list, items)
    items_set = set(items)
    return True if len(items_set) <= 1 else False

