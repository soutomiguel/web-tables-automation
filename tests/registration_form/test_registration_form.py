import time
from pages.registration_form_page import RegistrationPage
from utils.temp_data import temp_data
from utils.json_pointers import pointer_registration_incorrect_email_format

class TestRegistrationForm:
    def test_TC001_submit_form_with_valid_info(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.add()
        registration_page.fill_first_name()
        registration_page.fill_last_name()
        registration_page.fill_email()
        registration_page.fill_age()
        registration_page.fill_salary()
        registration_page.fill_department()
        registration_page.submit()
        time.sleep(2)

    def test_TC002_submit_without_data_populated(self, driver):
        pass

    def test_TC003_submit_form_with_incorrect_format_email(self, driver):
        pass