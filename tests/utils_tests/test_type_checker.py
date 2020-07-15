import pytest
from utils.check_type import check_type


def test_integer_and_string():
    with pytest.raises(TypeError):
        check_type(int, "d")


def test_integer_and_float():
    with pytest.raises(TypeError):
        check_type(int, 3.2)


def test_list_and_dict():
    with pytest.raises(TypeError):
        check_type(list, {"key": "value"})


def test_two_ints():
    assert check_type(int, 1) is None


def test_int_and_rounded_float():
    assert check_type(int, round(1.3)) is None


def test_one_argument():
    with pytest.raises(TypeError):
        check_type(1)


def test_no_arguments():
    with pytest.raises(TypeError):
        check_type()