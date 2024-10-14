from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import json_pointers

class RegistrationPage(BasePage):
    dashboard = json_pointers.pointer_dashboard_elements()
    registration = json_pointers.pointer_registration_form_elements()

    ADD_BTN = (By.ID, dashboard.buttons.add)
    FIRST_NAME = (By.ID, registration.inputs.firstName)
    LAST_NAME = (By.ID, registration.inputs.lastName)
    EMAIL = (By.ID, registration.inputs.email)
    AGE = (By.ID, registration.inputs.age)
    SALARY = (By.ID, registration.inputs.salary)
    DEPARTMENT = (By.ID, registration.inputs.departament)
    SUBMIT_BTN = (By.ID, registration.buttons.submit)

    def __init__(self, driver):
        super().__init__(driver)