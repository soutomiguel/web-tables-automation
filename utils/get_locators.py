import json

def read_json_file(locators):
    with open(locators, 'r') as r:
        return json.load(r)