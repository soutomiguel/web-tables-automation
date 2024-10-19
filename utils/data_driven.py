from dataclasses import dataclass, asdict
from utils.read_json import read_json_file

@dataclass
class CorrectInputs:
    firstName: str = None
    lastName: str = None
    email: str = None
    age: str = None
    salary: str = None
    department: str = None

@dataclass
class IncorrectFormat:
    email: str = None
    age: str = None
    salary: str = None

def load_correct_register_form(json_file):
    data = read_json_file('data', json_file)
    correct_inputs = CorrectInputs(**data['correct'])
    return correct_inputs

def load_incorrect_email_format(json_file):
    data = read_json_file('data', json_file)
    incorrect_email_format = IncorrectFormat(**data['incorrect_format'])
    return incorrect_email_format