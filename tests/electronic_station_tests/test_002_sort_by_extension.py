import pytest
from electronic_station.task_002_sort_by_extension import sort_by_extension
from hypothesis import given, settings, Verbosity, strategies as st


@given(extension1=st.text(alphabet=st.characters(min_codepoint=0, max_codepoint=100), min_size=1),
       extension2=st.text(alphabet=st.characters(min_codepoint=101, max_codepoint=104), min_size=1),
       extension3=st.text(alphabet=st.characters(min_codepoint=105, max_codepoint=108), min_size=1),
       extension4=st.text(alphabet=st.characters(min_codepoint=109, max_codepoint=112), min_size=1)
       )
@settings(verbosity=Verbosity.verbose)
def test_basic_extensions(extension1, extension2, extension3, extension4):
    files_list = ["spam." + extension4, "eggs." + extension2, "foo." + extension3, "bar." + extension1]
    expected_result = ["bar." + extension1, "eggs." + extension2, "foo." + extension3, "spam." + extension4]
    assert sort_by_extension(files_list) == expected_result, "Simple extensions"


@given(extension1=st.text(alphabet=st.characters(min_codepoint=0, max_codepoint=100), min_size=1),
       extension2=st.text(alphabet=st.characters(min_codepoint=101, max_codepoint=104), min_size=1),
       extension3=st.text(alphabet=st.characters(min_codepoint=105, max_codepoint=108), min_size=1))
@settings(verbosity=Verbosity.verbose)
def test_complex_extensions(extension1, extension2, extension3):
    files_list = ["spam.bot." + extension3, "foo.bar." + extension1, "eggs." + extension2]
    expected_result = ["foo.bar." + extension1, "eggs." + extension2, "spam.bot." + extension3]
    assert sort_by_extension(files_list) == expected_result, "Double extensions"


@given(extension=st.text(alphabet=st.characters(blacklist_categories=("Zs", "P")), min_size=1))
@settings(verbosity=Verbosity.verbose)
def test_file_with_no_extension(extension):
    # TODO: Investigate
    files_list = ["eggs", "foo.", "bar." + extension, ".spam"]
    expected_result = ["eggs", "foo.", ".spam", "bar." + extension]
    assert sort_by_extension(files_list) == expected_result, "Files without extension"


@given(test_list=st.lists(st.one_of(st.none(), st.integers(), st.floats(), st.booleans(), st.binary())))
@settings(verbosity=Verbosity.verbose)
def test_invalid_file_list(test_list):
    with pytest.raises(TypeError):
        sort_by_extension(test_list)


def test_no_args():
    with pytest.raises(TypeError):
        sort_by_extension()


def test_incorrect_args():
    with pytest.raises(TypeError):
        sort_by_extension(454345)

