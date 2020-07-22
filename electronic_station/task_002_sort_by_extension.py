"""
You are given a list of files.
You need to sort this list by the file extension.
The files with the same extension should be sorted by name.

Some possible cases:

    Filename cannot be an empty string;
    Files without the extension should go before the files with one;
    Filename ".config" has an empty extension and a name ".config";
    Filename "config." has an empty extension and a name "config.";
    Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
    Filename ".imp.xls" has an extension "xls" and a name ".imp".
https://py.checkio.org/ru/mission/sort-by-extension/
"""
from utils.check_type import check_type
from typing import List


def sort_by_extension(files: List[str]) -> List[str]:
    """
    Sorts given list of files by their extension
    :param files: A list of strings representing files
    :return: A list sorted by files extension
    """
    validate_files_list(files)

    filenames_with_extensions = get_filenames_with_extensions(files)
    filenames_without_extensions = get_filenames_without_extensions(files)

    sorted_filenames_with_extensions = sort_filenames_with_extension(filenames_with_extensions)
    sorted_filenames_without_extensions = sort_filenames_without_extensions(filenames_without_extensions)

    resulted_list = sorted_filenames_without_extensions + sorted_filenames_with_extensions
    return resulted_list


def validate_files_list(files: list) -> None:
    """
    Checks that all items in files list belong to 'str' type
    :param files: A list of files to validate
    :return: "Ok!" if list is correct, otherwise raises TypeError
    """
    check_type(list, files)
    if not files:
        raise TypeError("List is empty")
    for item in files:
        check_type(str, item)
    return


def get_filenames_with_extensions(files: list) -> list:
    """
    Gets filenames with extensions from files list
    :param files: A list of files
    :return: List of filenames with extensions
    """
    filenames_with_extensions = []

    for file in files:
        splitted_filename = file.split(".")
        if len(splitted_filename) > 1 and splitted_filename[-1] and splitted_filename[0]:
            filenames_with_extensions.append(file)

    return filenames_with_extensions


def get_filenames_without_extensions(files: list) -> list:
    """
    Gets filenames without extensions from files list
    :param files: A list of files
    :return: A list of filenames without extensions
    """
    filenames_without_extensions = []
    for file in files:
        splitted_filename = file.split(".")
        if len(splitted_filename) == 1 or not splitted_filename[-1] or not splitted_filename[0]:
            filenames_without_extensions.append(file)

    return filenames_without_extensions


def sort_filenames_with_extension(filenames_with_extension: list) -> list:
    """
    Sorts list of filenames with extensions
    :param filenames_with_extension: A list of filenames with extensions
    :return: Sorted list of filenames with extensions
    """
    return sorted(filenames_with_extension, key=lambda file: file.split(".")[-1])


def sort_filenames_without_extensions(filenames_without_extensions: list):
    """
    Sorts list of filenames without extensions
    :param filenames_without_extensions: A list of filenames without extensions
    :return: Sorted list of filenames without extensions
    """
    return sorted(filenames_without_extensions)
