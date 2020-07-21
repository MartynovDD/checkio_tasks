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
    check_type(list, files)
    validate_files_list(files)

    splitted_files = [file.split(".") for file in files]
    sorted_splitted_files = sorted(splitted_files, key=lambda file: file[-1] if len(file) > 1 and not file[-2] else file[0])
    resulted_list = [".".join(file) for file in sorted_splitted_files]
    return resulted_list


def validate_files_list(files: list) -> str:
    """
    Checks that all items in files list belong to 'str' type
    :param files: A list of files to validate
    :return: "Ok!" if list is correct, otherwise raises TypeError
    """
    if not files:
        raise TypeError("List is empty")
    for item in files:
        check_type(str, item)
    return "Ok!"
