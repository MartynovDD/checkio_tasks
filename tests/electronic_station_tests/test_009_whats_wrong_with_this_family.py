import pytest
from electronic_station.task_009_whats_wrong_with_this_family import is_family
from hypothesis import given, settings, Verbosity, assume, example, strategies as st

name_strategy = st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu")))


def test_father_and_son():
    assert is_family([["Alex", "Jake"]]), "Father and son"


@given(st.data())
@settings(verbosity=Verbosity.verbose)
def test_two_sons(data):
    father = data.draw(name_strategy)
    first_son = data.draw(name_strategy)
    second_son = data.draw(name_strategy)

    assume(father != first_son)
    assume(father != second_son)
    assume(first_son != second_son)

    tree = [[father, first_son], [father, second_son]]

    assert is_family(tree), "Two sons of one father"


def test_grandfather():
    tree = [["Alex", "Jake"], ["Alex", "William"], ["William", "Ron"]]
    assert is_family(tree), "Grandfather and grandson"


@given(name=name_strategy)
@settings(verbosity=Verbosity.verbose)
def test_equal_names(name):
    father = son = name
    tree = [[father, son]]

    assert not is_family(tree), "Equal names"


def test_father_to_father():
    tree = [["Alex", "Jake"], ["Alex", "Ron"], ["Ron", "Alex"]]
    assert not is_family(tree), "Second brother is father of father"


def test_father_to_brother():
    tree = [["Alex", "Jake"], ["Alex", "Ron"], ["Ron", "Jake"]]

    assert not is_family(tree), "Second brother is father of first brother"


def test_strangers_in_family():
    tree = [["Alex", "Jake"], ["Jake", "Ron"], ["Mario", "Luigi"]]
    assert not is_family(tree)


@given(tree=st.lists(st.lists(st.nothing())))
@settings(verbosity=Verbosity.verbose)
def test_empty_lists(tree):
    with pytest.raises(ValueError):
        is_family(tree)


def test_no_arguments():
    with pytest.raises(TypeError):
        is_family()


@given(tree=st.iterables(st.iterables(st.one_of(st.integers(), st.floats(), st.none(), st.booleans()))))
@settings(verbosity=Verbosity.verbose)
def test_incorrect_args(tree):
    with pytest.raises(TypeError):
        is_family(tree)
