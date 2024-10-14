import time
from pages.registration_form_page import RegistrationPage
from utils.json_pointers import pointer_registration_form_inputs

def test_submit_form_with_valid_info(driver):
    # Initializations
    data_driven = pointer_registration_form_inputs()
    registration_page = RegistrationPage(driver)

    registration_page.click(registration_page.ADD_BTN)
    registration_page.fill(registration_page.FIRST_NAME, data_driven.firstName)
    registration_page.fill(registration_page.LAST_NAME, data_driven.lastName)
    registration_page.fill(registration_page.EMAIL, data_driven.email)
    registration_page.fill(registration_page.AGE, data_driven.age)
    registration_page.fill(registration_page.SALARY, data_driven.salary)
    registration_page.fill(registration_page.DEPARTMENT, data_driven.department)
    registration_page.click(registration_page.SUBMIT_BTN)