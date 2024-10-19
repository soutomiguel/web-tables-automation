import time
from pages.dashboard_page import DashboardPage
from pages.registration_form_page import RegistrationPage

class TestRegistrationForm:
    def test_TC001_submit_form_with_valid_info(self, driver):
        registration_page = RegistrationPage(driver)
        dashboard_page = DashboardPage(driver)
        dashboard_page.add()
        registration_page.fill_first_name()
        registration_page.fill_last_name()
        registration_page.fill_email()
        registration_page.fill_age()
        registration_page.fill_salary()
        registration_page.fill_department()
        registration_page.submit()

    def test_TC002_submit_without_data_populated(self, driver):
        registration_page = RegistrationPage(driver)
        dashboard_page = DashboardPage(driver)
        dashboard_page.add()
        registration_page.submit()

    def test_TC003_submit_form_with_incorrect_email_format(self, driver):
        registration_page = RegistrationPage(driver)
        dashboard_page = DashboardPage(driver)
        dashboard_page.add()
        registration_page.fill_first_name()
        registration_page.fill_last_name()
        registration_page.fill_incorrect_email_format()
        registration_page.fill_age()
        registration_page.fill_salary()
        registration_page.fill_department()
        registration_page.submit()

    def test_TC004_submit_form_with_incorrect_age_format(self, driver):
        registration_page = RegistrationPage(driver)
        dashboard_page = DashboardPage(driver)
        dashboard_page.add()
        registration_page.fill_first_name()
        registration_page.fill_last_name()
        registration_page.fill_email()
        registration_page.fill_incorrect_age_format()
        registration_page.fill_salary()
        registration_page.fill_department()
        registration_page.submit()