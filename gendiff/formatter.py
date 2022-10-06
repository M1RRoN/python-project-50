"""Formatter module - formatting the tree with the selected formatter"""

from gendiff.formatters import format_stylish, format_plain, format_json


def formatting(tree: dict, format_name="stylish") -> str:
    """Formatting the tree with the selected formatter."""
    formats = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json,
    }
    if format_name in formats:
        return formats[format_name](tree)

    raise ValueError(f'Unknown format: {format_name}')
