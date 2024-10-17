from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import json_pointers
from utils.json_pointers import (
    pointer_registration_form,
    pointer_registration_incorrect_email_format
)

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_page = BasePage

    data_driven_TC001 = pointer_registration_form()
    data_driven_TC002 = pointer_registration_incorrect_email_format()
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

    def add(self):
        self.base_page.click(self, self.ADD_BTN)

    def fill_first_name(self):
        self.base_page.fill(self, self.FIRST_NAME, self.data_driven_TC001.firstName)

    def fill_last_name(self):
        self.base_page.fill(self, self.LAST_NAME, self.data_driven_TC001.lastName)

    def fill_email(self):
        self.base_page.fill(self, self.EMAIL, self.data_driven_TC001.email)

    def fill_age(self):
        self.base_page.fill(self, self.AGE, self.data_driven_TC001.age)

    def fill_salary(self):
        self.base_page.fill(self, self.SALARY, self.data_driven_TC001.salary)

    def fill_department(self):
        self.base_page.fill(self, self.DEPARTMENT, self.data_driven_TC001.department)

    def submit(self):
        self.click(self.SUBMIT_BTN)