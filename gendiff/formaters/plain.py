from typing import Any, Union


def to_str(value: Any) -> [Union[str, int]]:
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    return f"'{value}'"


def build_plain_iter(diff: dict, path="") -> str:
    lines = list()
    for dictionary in diff:
        property = f"{path}{dictionary['key']}"

        if dictionary['operation'] == 'add':
            lines.append(f"Property '{property}' "
                         f"was added with value: "
                         f"{to_str(dictionary['new'])}")

        if dictionary['operation'] == 'removed':
            lines.append(f"Property '{property}' was removed")

        if dictionary['operation'] == 'nested':
            new_value = build_plain_iter(dictionary['value'], f"{property}.")
            lines.append(f"{new_value}")

        if dictionary['operation'] == 'changed':
            lines.append(f"Property '{property}' was updated. "
                         f"From {to_str(dictionary['old'])} to "
                         f"{to_str(dictionary['new'])}")
    return '\n'.join(lines)


def render_plain(diff: dict) -> str:
    return build_plain_iter(diff)
