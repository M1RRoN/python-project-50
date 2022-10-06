import os
from gendiff.parser import parse
from gendiff.tree import build_tree
from gendiff.formatters import formatting


def get_file_extension(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def get_file_data(file_path: str) -> str:
    file_extension = get_file_extension(file_path)
    file_data = parse(file_path, file_extension)
    return file_data


def generate_diff(file_path1: str,
                  file_path2: str,
                  format_name="stylish") -> str:
    dict_1 = dict(get_file_data(file_path1))
    dict_2 = dict(get_file_data(file_path2))
    tree = build_tree(dict_1, dict_2)
    diff = formatting(tree, format_name)
    return diff
