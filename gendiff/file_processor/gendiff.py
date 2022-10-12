from typing import Callable

from gendiff.file_processor.file_handler import explore_file
from gendiff.file_processor.data_loader import load_content
from gendiff.file_processor.diff_assembler import get_diff_tree
from gendiff.formatters.tree_render import visualize_diff_tree
from gendiff.formatters.tree_render import DEFAULT_FORMAT


def generate_diff(file_path1: str, file_path2: str, format: str = DEFAULT_FORMAT) -> Callable:  # noqa: E501
    """
    Description:
    ---
        Accumulates all the logic of the program - accepts the entered data
        and returns the differences in the selected format.

    Parameters:
    ---
        - first_file (str): Path to first file (absolute or relative).
        - second_file (str): Path to second file (absolute or relative).

        - format (str): Format for comparison (default: stylish).

    Raises:
    ---
        - ValueError: Unsupported file extension.
        - ValueError: Unsupported render format.
        - RuntimeError: Failed to open file.
        - RuntimeError: This file is not valid.

    Return:
    ---
        Visualized Difference Tree.
    """
    diff_tree = get_diff_tree(
        data1=load_content(*explore_file(file_path1)),
        data2=load_content(*explore_file(file_path2))
    )

    return visualize_diff_tree(diff_tree, format)
