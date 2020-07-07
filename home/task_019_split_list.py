"""
You have to split a given array into two arrays.
If it has an odd amount of elements, then the first array should have more elements.
If it has no elements, then two empty arrays should be returned.
https://py.checkio.org/ru/mission/split-list/
"""


def split_list(items: list) -> list:
    """
    Splits list into two lists.
    If length of the items list is odd, then len(first_list) > len(second_list)
    :param items: a list of items to split
    :return: list of two sublists
    """
    split_markers = divmod(len(items), 2)
    if not split_markers[1]:
        result = [[item for item in items[:split_markers[0]]],
                  [item for item in items[split_markers[0]:]]]
    else:
        result = [[item for item in items[:(len(items) - split_markers[0])]], 
                  [item for item in items[(split_markers[0] + 1):]]]
    return result
