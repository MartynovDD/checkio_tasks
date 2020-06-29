"""
You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.
"""


def safe_pawns(pawns: set) -> int:
    """
    Using set of pawn coordinates counts number of safe pawns
    :param pawns: set of pawn checkmate coordinates (ex: {a4, e1, h3})
    :return: int number of safe pawns
    """
    pawn_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawn_indexes.add((row, col))

    count = 0
    for row, col in pawn_indexes:
        is_safe = ((row - 1, col - 1) in pawn_indexes) or ((row - 1, col + 1) in pawn_indexes)
        if is_safe:
            count += 1
    return count


