import json as json_global


def render_json(diff) -> str:
    return json_global.dumps(diff)
