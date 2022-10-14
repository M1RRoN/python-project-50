import json as json_global


def render_json(diff: list[dict]) -> str:
    return json_global.dumps(diff)
