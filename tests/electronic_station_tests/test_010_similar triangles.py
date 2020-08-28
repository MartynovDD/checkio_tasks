import pytest
from electronic_station.task_010_similar_triangles import are_similar


def test_basic_similar_triangles():
    assert are_similar([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]), "Basic similar triangles"


def test_scaled_triangles():
    assert are_similar([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]), "Scaled similar triangles"


def test_mirrored_triangles():
    assert are_similar([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]), "Mirrored similar triangles"


def test_scaled_and_mirrored_triangles():
    assert are_similar([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]), "Scaled and mirrored triangles"


def test_non_similar_triangles():
    assert not are_similar([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]), "Non-similar triangles"


def test_not_a_triangle():
    assert not are_similar([(0, 0), (1, 2)], [(2, 0), (4, 4), (6, 0)]), "One of the triangles is not a triangle"


def test_empty_lists():
    assert not are_similar([], []), "Empty lists"


def test_empty_coordinates():
    assert not are_similar([(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)]), "Empty coordinates"


def test_no_args():
    with pytest.raises(ValueError):
        are_similar()


def test_incorrect_args():
    with pytest.raises(TypeError):
        are_similar("sdfsdfs", [("a", "b")])