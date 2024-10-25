from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def get_element(self, element):
        try:
            return WebDriverWait(self.driver, self.timeout)\
                .until(EC.element_to_be_clickable(element))
        except TimeoutException as err:
            print("Element not found", err)



    def click(self, element):
        element_to_be_clicked = self.get_element(element)
        if element_to_be_clicked:
            element_to_be_clicked.click()
        else:
            print("Element couldn't be clicked")

    try:
        def get_text(self, element):
            return self.get_element(element).text
    except TimeoutException as err:
        print("Text couldn't be retrieved", err)

    try:
        def fill(self, element, value):
            self.get_element(element).send_keys(value)
    except TimeoutException as err:
        print("Element couldn't be retrieved", err)