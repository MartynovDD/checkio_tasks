"""
You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.
"""


def is_safe(pawn_indexes: set, pawn: tuple) -> bool:
    """
    Using coordinates checks whether given pawn is safe
    :param pawn_indexes: Set of numeric coordinates of all pawns
    :param pawn: Tuple of coordinates of a pawn to be checked
    :return: True if pawn is safe, False otherwise
    """
    return ((pawn[0] - 1, pawn[1] - 1) in pawn_indexes) or ((pawn[0] - 1, pawn[1] + 1) in pawn_indexes)


def pawn_coordinates(pawns: set) -> set:
    """
    Converts pawns checkmate coordinates to numeric coordinates
    :param pawns: Set of pawns' checkmate coordinates
    :return: Set of pawns' numeric coordinates
    """
    return {(int(pawn[1]) - 1, ord(pawn[0]) - 97) for pawn in pawns}


def safe_pawns(pawns: set) -> int:
    """
    Using set of pawn coordinates counts number of safe pawns
    :param pawns: set of pawn checkmate coordinates (ex: {a4, e1, h3})
    :return: int number of safe pawns
    """
    pawn_indexes = pawn_coordinates(pawns)
    safe = []
    for row, column in pawn_indexes:
        if is_safe(pawn_indexes, (row, column)):
            safe.append((row, column))
    return len(safe)


