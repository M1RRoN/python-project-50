from typing import Any

from gendiff.file_processor.diff_assembler import (
    REMOVED, ADDED, UPDATED, NESTED
)


ADDED_TEMPLATE_PLAIN = "Property '{}' was added with value: {}"
REMOVED_TEMPLATE_PLAIN = "Property '{}' was removed"
UPDATED_TEMPLATE_PLAIN = "Property '{}' was updated. From {} to {}"
COMPLEX_VALUE = "[complex value]"
PATH = "{}.{}"


def render_plain(diff_tree: list) -> str:
    """
    Description:
    ---
        Rendering the diff tree to plain format.

    Parameters:
    ---
        - diff_tree (dict): The difference tree.

        - parent (str): The path of the changed value
        from the parent (default: '').
        - result (list): Initial result of aggregation (default: None).

    Return:
    ---
        String visualization of a tree in plain format.
    """
    rendered_data = render_nodes(diff_tree)
    return rendered_data


def render_nodes(diff: list, source='') -> str:

    result = []
    diff.sort(key=lambda node: node['key'])

    for node in diff:

        path = PATH.format(source, node['key']) if source else node['key']

        if node['node type'] == REMOVED:
            result.append(REMOVED_TEMPLATE_PLAIN.format(path))

        elif node['node type'] == ADDED:
            result.append(ADDED_TEMPLATE_PLAIN.format(
                path,
                validate_data(node['value']['new'])
            ))

        elif node['node type'] == UPDATED:
            result.append(UPDATED_TEMPLATE_PLAIN.format(
                path,
                validate_data(node['value']['old']),
                validate_data(node['value']['new'])
            ))

        elif node['node type'] == NESTED:
            result.append(render_nodes(node['children'], path))

    return '\n'.join(result)


def validate_data(value: Any) -> str:

    if isinstance(value, bool):
        valid_value = str(value).lower()
    elif value is None:
        valid_value = 'null'
    elif isinstance(value, int):
        valid_value = str(value)
    elif isinstance(value, dict):
        valid_value = COMPLEX_VALUE
    else:
        valid_value = f"'{value}'"

    return valid_value
