from utils.get_web_elements import (
    load_dashboard_elements,
    load_register_form_elements
)
from utils.data_driven import load_correct_register_form_inputs

# JSON Elements pointer functions
def pointer_dashboard_elements():
    return load_dashboard_elements('dashboard_elements')

def pointer_registration_form_elements():
    return load_register_form_elements('registration_form_elements')

# Data Driven Testing pointer functions
def pointer_registration_form_inputs():
    return load_correct_register_form_inputs('register_data')