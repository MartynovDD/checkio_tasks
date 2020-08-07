import random
from typing import Union


def generate_string_from_groups(*groups: Union[int, str, float, bool], length=1) -> str:
    """
    Generates string from characters in given groups
    :param groups: Groups of characters
    :param length: Target length of resulted string, default value - 1
    :return: String generated from groups
    """
    template = "".join([str(group) for group in groups])
    result_string = "".join((random.choice(template) for _ in range(length)))
    return result_string


if __name__ == "__main__":
    print(generate_string_from_groups("abcdef", 12345, length=6))
