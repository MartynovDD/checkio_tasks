import pytest
from utils.type_checker import type_checker


def test_integer_and_string():
    with pytest.raises(TypeError):
        type_checker(int, "d")


def test_integer_and_float():
    with pytest.raises(TypeError):
        type_checker(int, 3.2)


def test_list_and_dict():
    with pytest.raises(TypeError):
        type_checker(list, {"key": "value"})


def test_two_ints():
    assert type_checker(int, 1) is None


def test_int_and_rounded_float():
    assert type_checker(int, round(1.3)) is None


def test_one_argument():
    with pytest.raises(TypeError):
        type_checker(1)


def test_no_arguments():
    with pytest.raises(TypeError):
        type_checker()