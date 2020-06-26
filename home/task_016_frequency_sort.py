"""
Sort the given iterable so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
"""
import typing


def frequency_sort(items: typing.Iterable) -> list:
    # TODO Fix to pass test 3
    # TODO Add pytest tests
    """
    Sorts iterable by item frequency
    :param items: Iterable
    :return: list
    """
    result = sorted(items, key=items.count, reverse=True)
    return result

