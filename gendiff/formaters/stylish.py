from typing import Any

DEFAULT_INDENT = 4


def to_str(value: Any, depth: int) -> str:
    if isinstance(value, dict):
        lines = ['{']
        for key, nested_value in value.items():
            if isinstance(nested_value, dict):
                new_value = to_str(nested_value, depth + DEFAULT_INDENT)
                lines.append(f"{' ' * depth}    {key}: {new_value}")
            else:
                lines.append(f"{' ' * depth}    {key}: {nested_value}")
        lines.append(f'{" " * depth}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def line_forming(dictionary: dict, key: Any, depth: int, sign: str) -> str:
    return f'{" " * depth}{sign}{dictionary["key"]}: ' \
           f'{to_str(dictionary[key], depth + DEFAULT_INDENT)}'


def build_stylish_iter(diff: dict, depth=0) -> str:
    lines = ['{']
    for dictionary in diff:
        if dictionary['operation'] == 'same':
            lines.append(line_forming(
                dictionary, 'value',
                depth, sign='    '
            ))

        if dictionary['operation'] == 'add':
            lines.append(line_forming(
                dictionary, 'new',
                depth, sign='  + '
            ))

        if dictionary['operation'] == 'removed' or dictionary[
                'operation'] == 'changed':
            lines.append(line_forming(
                dictionary, 'old',
                depth, sign='  - '
            ))

        if dictionary['operation'] == 'changed':
            lines.append(
                line_forming(
                    dictionary, 'new',
                    depth, sign='  + '
                ))

        if dictionary['operation'] == 'nested':
            new_value = build_stylish_iter(dictionary['value'],
                                           depth + DEFAULT_INDENT)
            lines.append(
                f'{" " * depth}    {dictionary["key"]}: {new_value}')
    lines.append(f'{" " * depth}}}')
    return '\n'.join(lines)


def render_stylish(diff: dict) -> str:
    return build_stylish_iter(diff)
