from utils.get_elements import load_dashboard_elements, load_register_form_elements

def pointer_dashboard_elements():
    return load_dashboard_elements('dashboard_elements.json')

def pointer_registration_form_elements():
    return load_register_form_elements('registration_form_elements.json')