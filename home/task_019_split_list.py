"""
You have to split a given array into two arrays.
If it has an odd amount of elements, then the first array should have more elements.
If it has no elements, then two empty arrays should be returned.
https://py.checkio.org/ru/mission/split-list/
"""


def split_list(items: list) -> list:
    """
    Splits list into two lists.
    If length of the items list is odd, then len(first_list) < len(second_list)
    :param items: a list of items to split
    :return: list of two sublists
    """
    if len(items) % 2 == 0:
        first_length = int(len(items) / 2)
        second_length = first_length
    else:
        first_length = len(items) - int(len(items) / 2)
        second_length = int(len(items) / 2) + 1
    result = [[item for item in items[:first_length]], [item for item in items[second_length:]]]
    return result


if __name__ == "__main__":
    assert split_list([1, 2, 3, 4]) == [[1, 2], [3, 4]], "Even length"



