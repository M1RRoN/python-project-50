"""JSON module - apply JSON view to diff"""


import json


def format_(tree: list) -> json:
    return json.dumps(tree, indent=4)
