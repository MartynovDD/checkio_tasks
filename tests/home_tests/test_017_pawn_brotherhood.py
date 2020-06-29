import pytest
from home.task_017_pawn_brotherhood import safe_pawns


def test_six_safe():
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6, "Six safe pawns"


def test_one_safe():
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1, "One safe pawn"


def test_diagonal_pawns():
    assert safe_pawns({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"}) == 7, "Diagonal pawns"


def test_only_one_pawn():
    assert safe_pawns({"d2"}) == 0, "Only one pawn"


def test_equal_coordinates():
    assert safe_pawns({"b4", "b4", "d4", "f4", "f4", "c3", "e3", "g5", "d2"}) == 6, "Equal cooridnates"


def test_no_arguments():
    with pytest.raises(TypeError):
        safe_pawns()


def test_incorrect_arguments():
    with pytest.raises(TypeError):
        safe_pawns(4354)


def test_insufficient_coords():
    with pytest.raises(TypeError):
        safe_pawns({1, 4, 5, 7})


def test_empty_set():
    assert safe_pawns(set()) == 0, "Empty set"
