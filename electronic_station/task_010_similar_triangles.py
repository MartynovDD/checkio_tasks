"""
You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

Input:
    Two lists as coordinates of vertices of each triangle.
    Coordinates is three tuples of two integers.

Output: True or False.

Precondition:

    -10 ≤ x(, y) coordinate ≤ 10

"""
from typing import List, Tuple


def are_similar(first_coords: List[Tuple[int, int]], second_coords: List[Tuple[int, int]]) -> bool:
    """
    Checks if two given triangles are similar
    :param first_coords: Coordinates of the first triangle
    :param second_coords: Coordinates of the second triangle
    :return: True if triangles are similar, otherwise False
    """
    # Step 1: Get angles of each triangle
    # Step 2: Compare grades of two triangles
    # Step 3: If two angles are equal then first triangle is similar to second triangle
    pass
