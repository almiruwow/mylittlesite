import json


def json_d():
    with open("candidates.json", "r") as f:
        text_json = json.load(f)
    return text_json