from selenium.webdriver.common.by import By
from pages.registration_form_page import RegistrationPage
from utils import json_pointers_for_tests

def test_main(driver):
    dashboard = json_pointers_for_tests.pointer_dashboard_elements()
    registration = json_pointers_for_tests.pointer_registration_form_elements()
    registration_page = RegistrationPage(driver)
    registration_page.click((By.ID, dashboard.buttons.add))
    registration_page.fill((By.ID, registration.inputs.firstName), "data driven test")