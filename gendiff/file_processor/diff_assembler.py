from typing import Any, Optional


ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'


def get_diff_tree(data1: dict, data2: dict) -> dict:
    """
    Description:
    ---
        Accepts two dictionaries as input and makes a difference tree.

    Parameters:
    ---
        - data1 (dict): Data of the first file as a Python dictionary.
        - data2 (dict): Data of the second file as a Python dictionary.

    Return:
    ---
        diff_tree (dict): The difference tree of the first file (data1)
        and the second file (data2).
    """
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff_tree = []
    for key in all_keys:

        if key in data1 and key not in data2:
            diff_tree.append(add_node(key, REMOVED, old_value=data1[key]))

        elif key not in data1 and key in data2:
            diff_tree.append(add_node(key, ADDED, value=data2[key]))

        elif data1[key] == data2[key]:
            diff_tree.append(add_node(key, UNCHANGED, old_value=data1[key]))

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            child_diff = get_diff_tree(data1[key], data2[key])
            diff_tree.append(add_node(key, NESTED, children=child_diff))

        else:
            diff_tree.append(
                add_node(key, UPDATED, value=data2[key], old_value=data1[key])
            )

    return diff_tree


def add_node(key: Any, node_type: str,
             value: Any = None, old_value: Any = None,
             children: Optional[list] = None) -> dict:

    node = {
        'key': key,
        'value': {
            'old': old_value,
            'new': value
        },
        'node type': node_type
    }

    if children is not None:
        node['children'] = children

    return node
