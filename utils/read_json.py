import json
import os

def read_json_file(directory, file):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, '..', directory, f'{file}.json')

    with open(file_path, 'r') as elements_json:
        return json.load(elements_json)