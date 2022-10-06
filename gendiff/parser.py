import json
import yaml


def parse(data, format_name):
    if format_name == '.json':
        return json.load(open(data))
    if format_name in ('.yml', '.yaml'):
        return yaml.safe_load(open(data))

    raise ValueError('Unknown file format')
