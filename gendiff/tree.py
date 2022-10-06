"""Build internal tree view"""


def make_tree(dict_1: dict, dict_2: dict) -> list:
    keys = dict_1.keys() | dict_2.keys()

    result = []
    for key in sorted(keys):
        child_1 = dict_1.get(key)
        child_2 = dict_2.get(key)

        if key not in dict_1:
            result.append({
                'key': key,
                'type': 'added',
                'value': child_2
            })
        elif key not in dict_2:
            result.append({
                'key': key,
                'type': 'removed',
                'value': child_1
            })
        elif isinstance(child_1, dict) and isinstance(child_2, dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': make_tree(child_1, child_2),
            })
        elif child_1 == child_2:
            result.append({
                'key': key,
                'type': 'unchanged',
                'value': child_1,
            })
        else:
            result.append({
                'key': key,
                'type': 'changed',
                'old_value': child_1,
                'new_value': child_2,
            })

    return result


def build_tree(dict_1: dict, dict_2: dict):
    return {
        'type': 'root',
        'children': make_tree(dict_1, dict_2)
    }
