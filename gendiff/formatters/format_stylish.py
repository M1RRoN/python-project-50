from typing import Any

from gendiff.file_processor.diff_assembler import (
    REMOVED, ADDED, UNCHANGED, UPDATED, NESTED
)


STARTLINE_TEMPLATE = '{}{} {}: {{'
DIFFLINE_TEMPLATE = '{}{} {}: {}'
ENDLINE_TEMPLATE = '{}  }}'
FRAME_TEMPLATE = '{{\n{}\n}}'
NESTING_INDENTATION = 4
SIGN_SPACING = 2


def render_stylish(diff_tree: dict) -> str:
    """
    Description:
    ---
        Rendering the diff tree to stylish format.

    Parameters:
    ---
        - diff_tree (dict): The difference tree.

        - diff_depth (int): Indentation value for a line (default: 0).

    Return:
    ---
        result (str): String visualization of a tree in stylish format.
    """
    rendered_data = FRAME_TEMPLATE.format(render_nodes(diff_tree))
    return rendered_data


def render_nodes(diff: list, level: int = 1) -> str:  # noqa: C901

    result = []
    indent = calculate_indent(level)
    diff.sort(key=lambda node: node['key'])

    for node in diff:

        if node['node type'] == REMOVED:
            result.append(compose_line(
                node['key'], node['value']['old'], '-', level
            ))

        elif node['node type'] == ADDED:
            result.append(compose_line(
                node['key'], node['value']['new'], '+', level
            ))

        elif node['node type'] == UNCHANGED:
            result.append(compose_line(
                node['key'], node['value']['old'], ' ', level
            ))

        elif node['node type'] == UPDATED:
            result.append(compose_line(
                node['key'], node['value']['old'], '-', level
            ))
            result.append(compose_line(
                node['key'], node['value']['new'], '+', level
            ))

        elif node['node type'] == NESTED:
            result.extend([
                STARTLINE_TEMPLATE.format(indent, ' ', node['key']),
                render_nodes(node['children'], level + 1),
                ENDLINE_TEMPLATE.format(indent)
            ])

    return '\n'.join(result)


def calculate_indent(level: int) -> str:

    return ' ' * (level * NESTING_INDENTATION - SIGN_SPACING)


def compose_line(key: Any, value: Any, sign: str, level: int) -> str:

    result = []
    indent = calculate_indent(level)
    level += 1

    if isinstance(value, dict):
        result.extend([
            STARTLINE_TEMPLATE.format(indent, sign, key),
            formate_dict_value(value, level),
            ENDLINE_TEMPLATE.format(indent)
        ])

    else:
        result.append(DIFFLINE_TEMPLATE.format(
            indent, sign, key, validate_data(value)
        ))

    return '\n'.join(result)


def formate_dict_value(dict_value: dict, level: int) -> str:

    result = []

    for key, value in dict_value.items():
        result.append(compose_line(key, value, ' ', level))

    return '\n'.join(result)


def validate_data(value: Any) -> str:

    if isinstance(value, bool):
        valid_value = str(value).lower()
    elif value is None:
        valid_value = 'null'
    else:
        valid_value = str(value)

    return valid_value
