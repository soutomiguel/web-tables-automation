import json
import os
from dataclasses import dataclass

@dataclass
class Buttons:
    add: str = None
    submit: str = None

@dataclass
class Inputs:
    firstName: str = None
    lastName: str = None
    email: str = None
    age: str = None
    salary: str = None
    departament: str = None

@dataclass
class DashboardElements:
    buttons: Buttons

@dataclass
class RegistrationFormElements:
    inputs: Inputs
    buttons: Buttons

def read_json_file(file):
    base_path = os.path.dirname(__file__)
    jsons_folder = os.path.join(base_path, '..', 'elements')
    file_path = os.path.join(jsons_folder, file)

    with open(file_path, 'r') as web_elements_file:
        return json.load(web_elements_file)

def load_dashboard_elements(json_file):
    data = read_json_file(json_file)
    buttons = Buttons(**data['buttons'])
    return DashboardElements(buttons=buttons)

def load_register_form_elements(json_file):
    data = read_json_file(json_file)
    inputs = Inputs(**data['inputs'])
    buttons = buttons = Buttons(**data['buttons'])
    return RegistrationFormElements(inputs=inputs, buttons=buttons)