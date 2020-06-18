"""
You have a table with all available goods in the store.
The data is represented as a list of dicts

Your mission here is to find the TOP most expensive goods.
The amount we are looking for will be given as a first argument and the whole data as the second one
https://py.checkio.org/en/mission/bigger-price/
"""


def bigger_price(limit: int, data: list) -> list:
    """
    Get most expensive item from list of dicts
    """
    data = sorted(data, key=lambda item: item.get("price"), reverse=True)
    return data[:limit]


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
