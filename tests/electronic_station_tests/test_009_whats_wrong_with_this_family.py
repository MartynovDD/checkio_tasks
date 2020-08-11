import pytest
from electronic_station.task_009_whats_wrong_with_this_family import is_family
from hypothesis import given, settings, Verbosity, example, strategies as st


@given(father_and_son=st.lists(st.lists(st.text(st.characters(whitelist_categories=("Ll", "Lu"))),
                                        st.text(st.characters(whitelist_categories=("Ll", "Lu"))),
                                        unique=True, min_size=2),
                               min_size=1))
@example(father_and_son=[["Alex", "Jake"]])
@settings(verbosity=Verbosity.verbose)
def test_father_and_son(father_and_son):
    assert is_family(father_and_son), "Father and son"


@given(father=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))),
       son=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))))
@settings(verbosity=Verbosity.verbose)
def test_two_sons(father, son):
    first_son = st.shared(son)
    second_son = st.shared(son)
    people = [[father, first_son], [father, second_son]]

    assert is_family(people), "Two sons of one father"


@given(father=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))),
       son=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))))
@settings(verbosity=Verbosity.verbose)
def test_grandfather(father, son):
    first_brother = st.shared(son)
    second_brother = st.shared(son)
    son_of_second_brother = st.shared(second_brother)
    people = [[father, first_brother], [father, second_brother], [second_brother, son_of_second_brother]]

    assert is_family(people), "Grandfather and grandson"


@given(father=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))),
       son=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))))
@settings(verbosity=Verbosity.verbose)
def test_father_to_father(father, son):
    first_brother = st.shared(son)
    second_brother = st.shared(son)
    people = [[father, first_brother], [father, second_brother], [second_brother, father]]

    assert not is_family(people), "Second brother is father of father"


@given(father=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))),
       son=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))))
@settings(verbosity=Verbosity.verbose)
def test_father_to_brother(father, son):
    first_brother = st.shared(son)
    second_brother = st.shared(son)
    people = [[father, first_brother], [father, second_brother], [second_brother, first_brother]]

    assert not is_family(people), "Second brother is father of first brother"


@given(father=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))),
       son=st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu"))))
@settings(verbosity=Verbosity.verbose)
def test_strangers_in_family(father, son):
    first_brother = st.shared(son)
    second_brother = st.shared(son)
    son_of_second_brother = st.shared(second_brother)
    unknown_father = st.shared(father)
    unknown_son = st.shared(son)
    people = [[father, first_brother],
              [father, second_brother],
              [second_brother, son_of_second_brother],
              [unknown_father, unknown_son]]

    assert not is_family(people)


@given(people=st.lists(st.lists(st.nothing())))
@settings(verbosity=Verbosity.verbose)
def test_empty_lists(people):
    assert not is_family(people), "Empty lists"


def test_no_arguments():
    with pytest.raises(TypeError):
        is_family()


@given(people=st.iterables(st.iterables(st.integers(), st.floats(), st.none(), st.booleans())))
@settings(verbosity=Verbosity.verbose)
def test_incorrect_args(people):
    with pytest.raises(TypeError):
        is_family()
