import json

from gendiff.file_processor.diff_assembler import (
    REMOVED, ADDED, UNCHANGED, UPDATED, NESTED
)


def render_json(diff_tree: dict) -> str:
    """
    Description:
    ---
        Rendering the diff tree to JSON format.

    Parameters:
    ---
        - diff_tree (dict): The difference tree.

    Return:
    ---
        String visualization of a tree in JSON format.
    """
    rendered_data = json.dumps(render_nodes(diff_tree), indent=4)
    return rendered_data


def render_nodes(diff: list) -> dict:

    result = {}
    diff.sort(key=lambda node: node['key'])

    for node in diff:

        if node['node type'] in (REMOVED, UNCHANGED):
            result[node['key']] = {
                'value': node['value']['old']
            }

        elif node['node type'] == ADDED:
            result[node['key']] = {
                'value': node['value']['new']
            }

        elif node['node type'] == UPDATED:
            result[node['key']] = {
                'value': {
                    'old': node['value']['old'],
                    'new': node['value']['new']
                }
            }

        elif node['node type'] == NESTED:
            result[node['key']] = {
                'value': render_nodes(node['children'])
            }

        result[node['key']]['node type'] = node['node type'].upper()

    return result
