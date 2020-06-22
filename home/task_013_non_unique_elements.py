"""
You are given a non-empty list of integers (X).
For this task, you should return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are contained in a given list only once).
When solving this task, do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
https://py.non_unique_elements.org/en/mission/non-unique-elements/
"""
from utils.exception_catcher import exception_catcher


def non_unique_elements(data: list) -> list:
    """
    Delete all unique elements from list and return list
    """
    if isinstance(data, dict):
        data = list(data.values())
    result_list = [item for item in data if data.count(item) > 1]
    return result_list


if __name__ == "__main__":
    assert non_unique_elements([1, 2, 3, 4, 5]) == [], "Only unique elements"
    assert non_unique_elements([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "Only non-unique elements"
    assert non_unique_elements([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "One unique element"
    assert non_unique_elements(["hello", "hello", "world"]) == ["hello", "hello"], "Words"
    assert non_unique_elements([1 + 1, 2, 0, 1, 0 + 1]) == [2, 2, 1, 1], "1 + 1, 0 + 1"
    assert non_unique_elements([1.1 + 2.2, 3.3]) == [], "Floats"
    assert non_unique_elements([]) == [], "Empty list"
    assert non_unique_elements({"first" : 1, "second" : 1, "third" : 3}) == [1, 1], "Dictionary"
    assert non_unique_elements("aaaagggrty") == ["a", "a", "a", "a", "g", "g", "g"], "A string"
    assert non_unique_elements("") == [], "Empty string"
    assert non_unique_elements(["", "", "", "a"]) == ["", "", ""], "List with empty strings"
    assert exception_catcher(non_unique_elements) == TypeError, "No arguments"
    assert exception_catcher(non_unique_elements, 53556) == TypeError, "Incorrect argument"
