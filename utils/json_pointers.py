from utils.get_web_elements import (
    load_dashboard_elements,
    load_register_form_elements
)
from utils.data_driven import (
    load_correct_register_form, load_incorrect_email_format
)

# JSON pointers
def pointer_dashboard_elements():
    return load_dashboard_elements('dashboard_elements')

def pointer_registration_form_elements():
    return load_register_form_elements('registration_form_elements')

# Data Driven Testing pointers
def pointer_registration_form():
    return load_correct_register_form('register_data')

def pointer_registration_incorrect_format():
    return load_incorrect_email_format('register_data')

