from typing import Callable
import json

import yaml


TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')
UNSUPPORTED_TYPE = '''Extension "{}" is not supported.
Use JSON or YML/YAML format'''
INVALID_FILE = '''This file is not valid.
Please, make sure the file is filled in correctly.'''


def load_content(content: str, data_format: str) -> Callable:
    """
    Description:
    ---
        Loads data based on the passed extension.

    Parameters:
    ---
        - content (str): Data from a file as a string.
        - data_format (str): File extension.

    Raises:
    ---
        - ValueError: Unsupported file extension.
        - RuntimeError: This file is not valid.

    Return:
    ---
        data (dict): Converts document to Python dictionary object.
    """
    if data_format == TYPE_JSON:
        return load_json(content)
    elif data_format in TYPE_YML_OR_YAML:
        return load_yaml(content)
    else:
        raise ValueError(UNSUPPORTED_TYPE.format(data_format))


def load_json(content: str) -> dict:

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise RuntimeError(INVALID_FILE)


def load_yaml(content: str) -> dict:

    try:
        return yaml.load(content, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        raise RuntimeError(INVALID_FILE)
