"""
You have a table with all available goods in the store.
The data is represented as a list of dicts

Your mission here is to find the TOP most expensive goods.
The amount we are looking for will be given as a first argument and the whole data as the second one
https://py.checkio.org/en/mission/bigger-price/
"""
import decimal
from utils.exception_catcher import exception_catcher


def sort_key(dict_list: list):
    return lambda item: item.get("price") if item.get("price") else 0


def format_price(dict_list: list) -> list:
    for item in dict_list:
        if not item.get("price"):
            continue
        if not isinstance(item.get("price"), int):
            item.update(
                price=float(
                    decimal.Decimal(item.get("price")).quantize(decimal.Decimal(".1"), rounding=decimal.ROUND_DOWN)))
    return dict_list


def bigger_price(limit: int, data: list) -> list:
    """
    Get most expensive item from list of dicts
    """
    sorted_data = sorted(data, key=sort_key(data), reverse=True)
    return format_price(sorted_data[:limit])


if __name__ == "__main__":
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
               {"name": "wine", "price": 138},
               {"name": "bread", "price": 100}
           ], "Two most expensive goods"
    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "One most expensive good"

    assert bigger_price(10, [
        {"name": "iphone", "price": 200},
        {"name": "samsung", "price": 150},
        {"name": "meizu", "price": 100}
    ]) == [
               {"name": "iphone", "price": 200},
               {"name": "samsung", "price": 150},
               {"name": "meizu", "price": 100}
           ], "Limit out of range"

    assert bigger_price(-1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Negative index"

    assert bigger_price(0, [
        {"name": "Eggs", "price": 82}
    ]) == [], "Limit not given"

    assert bigger_price(1, [
        {"name": "spam"}
    ]) == [{"name": "spam"}], "No price"
    assert bigger_price(2, [
        {"name": "a", "price": 100},
        {"name": "c", "price": 100},
        {"name": "b", "price": 100}
    ]) == [{"name": "a", "price": 100}, {"name": "c", "price": 100}], "Equal price"
    assert bigger_price(2, [
        {"name": "a", "price": 1.1 + 2.2},
        {"name": "c", "price": 1.1 + 2.2},
        {"name": "b", "price": 1.1 + 2.2}
    ]) == [{"name": "a", "price": 3.3}, {"name": "c", "price": 3.3}], "Float equal price"
    assert exception_catcher(bigger_price) == TypeError, "Arguments not filled"
    assert exception_catcher(bigger_price, 4, 5) == TypeError, "Incorrect arguments"
    assert exception_catcher(bigger_price, 5) == TypeError, "Missing one argument"
