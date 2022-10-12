from typing import Callable

from gendiff.formatters.format_stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'
DEFAULT_FORMAT = FORMAT_STYLISH
FORMATS = (FORMAT_STYLISH, FORMAT_JSON, FORMAT_PLAIN)
UNSUPPORTED_FORMAT = '''Format is not supported.
Use STYLISH, PLAIN or JSON format'''


def visualize_diff_tree(diff_tree: dict, format: str) -> Callable:
    """
    Description:
    ---
        Activate the rendering function based on the selected format:
        stylish, plain or json.

    Parameters:
    ---
        - diff_tree (dict): The difference tree.
        - format: stylish/plain/json.

    Raises:
    ---
        - ValueError: Unsupported render format.

    Return:
    ---
        Calling the rendering function in the selected view.
    """
    if format == FORMAT_STYLISH:
        return render_stylish(diff_tree)
    elif format == FORMAT_PLAIN:
        return render_plain(diff_tree)
    elif format == FORMAT_JSON:
        return render_json(diff_tree)
    else:
        raise ValueError(UNSUPPORTED_FORMAT)
