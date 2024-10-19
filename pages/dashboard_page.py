from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils import json_pointers

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_page = BasePage

    dashboard = json_pointers.pointer_dashboard_elements()

    ADD_BTN = (By.ID, dashboard.buttons.add)

    def add(self):
        self.base_page.click(self, self.ADD_BTN)
