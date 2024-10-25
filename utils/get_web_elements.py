from dataclasses import dataclass
from utils.read_json import read_json_file

@dataclass
class Buttons:
    add: str = None
    submit: str = None
    close: str = None
    edit: str = None
    delete_1: str = None
    delete_2: str = None
    delete_3: str = None
    edit_record_1: str = None
    edit_record_2: str = None
    edit_record_3: str = None

@dataclass
class Inputs:
    firstName: str = None
    lastName: str = None
    email: str = None
    age: str = None
    salary: str = None
    departament: str = None
    search: str = None

@dataclass
class Values:
    first_name: str = None
    last_name: str = None
    email: str = None
    age: str = None
    salary: str = None
    department: str = None

@dataclass
class RGB_Colors:
    error: str = None

@dataclass
class DashboardElements:
    buttons: Buttons
    inputs: Inputs
    values: Values

@dataclass
class RegistrationFormElements:
    inputs: Inputs
    buttons: Buttons
    rgb_colors: RGB_Colors

def load_dashboard_elements(json_file):
    data = read_json_file('elements', json_file)
    buttons = Buttons(**data['buttons'])
    inputs = Inputs(search = data['inputs'])
    values = Values(**data['values'])
    return DashboardElements(buttons=buttons, inputs=inputs, values=values)

def load_register_form_elements(json_file):
    data = read_json_file('elements', json_file)
    inputs = Inputs(**data['inputs'])
    buttons = Buttons(**data['buttons'])
    colors = RGB_Colors(error = data['rgb'])
    return RegistrationFormElements(inputs=inputs, buttons=buttons, rgb_colors=colors)