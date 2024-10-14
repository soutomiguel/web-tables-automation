from dataclasses import dataclass
from utils.read_json import read_json_file

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

def load_dashboard_elements(json_file):
    data = read_json_file('elements', json_file)
    buttons = Buttons(**data['buttons'])
    return DashboardElements(buttons=buttons)

def load_register_form_elements(json_file):
    data = read_json_file('elements', json_file)
    inputs = Inputs(**data['inputs'])
    buttons = buttons = Buttons(**data['buttons'])
    return RegistrationFormElements(inputs=inputs, buttons=buttons)