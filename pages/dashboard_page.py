from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils import json_pointers

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_page = BasePage

    dashboard = json_pointers.pointer_dashboard_elements()

    ADD_BTN = (By.ID, dashboard.buttons.add)
    DELETE_1_BNT = (By.XPATH, dashboard.buttons.delete_1)
    DELETE_2_BNT = (By.XPATH, dashboard.buttons.delete_2)
    DELETE_3_BNT = (By.XPATH, dashboard.buttons.delete_3)
    EDIT_1_BNT = (By.XPATH, dashboard.buttons.edit_record_1)
    EDIT_2_BNT = (By.XPATH, dashboard.buttons.edit_record_2)
    EDIT_3_BNT = (By.XPATH, dashboard.buttons.edit_record_3)

    FIRST_NAME = (By.XPATH, dashboard.values.first_name)
    LAST_NAME = (By.XPATH, dashboard.values.last_name)
    AGE = (By.XPATH, dashboard.values.age)
    EMAIL = (By.XPATH, dashboard.values.email)
    SALARY = (By.XPATH, dashboard.values.salary)
    DEPARTMENT = (By.XPATH, dashboard.values.department)

    def add(self):
        self.base_page.click(self, self.ADD_BTN)

    def delete_initial_data(self):
        self.base_page.click(self, self.DELETE_1_BNT)
        self.base_page.click(self, self.DELETE_2_BNT)
        self.base_page.click(self, self.DELETE_3_BNT)

    def get_first_name_value(self):
        return self.base_page.get_text(self, self.FIRST_NAME)

    def get_last_name_value(self):
        return self.base_page.get_text(self, self.LAST_NAME)

    def get_age_value(self):
        return self.base_page.get_text(self, self.AGE)

    def get_email_value(self):
        return self.base_page.get_text(self, self.EMAIL)

    def get_salary_value(self):
        return self.base_page.get_text(self, self.SALARY)

    def get_department_value(self):
        return self.base_page.get_text(self, self.DEPARTMENT)