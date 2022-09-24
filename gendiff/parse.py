import json
import yaml
from yaml.loader import SafeLoader


def parser(file_path):
    format = (file_path.split('.'))[1]
    with open(file_path) as file:
        if format.lower() == 'json':
            return json.load(file)
        elif format.lower() == 'yml' or format.lower() == 'yaml':
            return yaml.load(file, Loader=SafeLoader)
