"""
In this mission you should check if all elements in the given list are equal.
https://py.checkio.org/en/mission/all-the-same/
"""
from utils.check_type import check_type


def all_the_same(items: list) -> bool:
    """
    Checks if all items in list are same
    :param items: a list of items to compare
    :return: True if all items are same, False if not
    """
    check_type(list, items)
    items_set = set(items)
    return True if len(items_set) <= 1 else False

