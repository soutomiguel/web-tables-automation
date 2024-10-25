import time
from time import sleep

from pages.dashboard_page import DashboardPage
from pages.registration_form_page import RegistrationPage

class TestRegistrationForm:
    def test_TC001_submit_form_with_valid_info(self, driver):
        registration_page = RegistrationPage(driver)
        dashboard_page = DashboardPage(driver)

        dashboard_page.delete_initial_data()
        dashboard_page.add()
        registration_page.fill_first_name()
        registration_page.fill_last_name()
        registration_page.fill_email()
        registration_page.fill_age()
        registration_page.fill_salary()
        registration_page.fill_department()
        registration_page.submit()

        assert (
            registration_page.
                data_driven_registration_correct_format.firstName == dashboard_page.get_first_name_value()
        )

    def test_TC002_submit_without_data_populated(self, driver):
        registration_page = RegistrationPage(driver)
        dashboard_page = DashboardPage(driver)

        dashboard_page.add()
        registration_page.submit()

        assert (
            registration_page.
                get_CSS_value('border-color') == registration_page.registration.rgb_colors.error
        )

    def test_TC006_close_form(self, driver):
        registration_page = RegistrationPage(driver)
        dashboard_page = DashboardPage(driver)

        dashboard_page.add()
        registration_page.close_registration_form()