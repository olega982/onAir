import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from framework.browser.driver_manager import DriverManager

REUSE_NUMBER = 2
DRIVER_WAIT_TIME = 5


def reuse(func):
    def wrapper(*args, **kwargs):
        for _ in range(REUSE_NUMBER):
            try:
                if func(*args, **kwargs):
                    break
            except ElementClickInterceptedException:
                print(f"One more try of:{__name__}")

    return wrapper


class BrowserWebElement:

    def __init__(self, locator_type, locator):
        self.__locator_type = locator_type
        self.__locator = locator

    def get_text(self):
        if self.is_element_present():
            return self.find_element().text
        else:
            "Element is not located"

    def verify_element_text(self, text):
        return WebDriverWait(DriverManager.get_driver(), DRIVER_WAIT_TIME).until(
            EC.text_to_be_present_in_element((self.__locator_type, self.__locator), text))

    def hover(self):
        self.is_element_present()
        hover = ActionChains(DriverManager.get_driver()).move_to_element(
            self.find_element())
        hover.perform()

    def is_enabled(self):
        if self.is_element_present():
            return DriverManager.get_driver().find_element(self.__locator_type, self.__locator).is_enabled()
        else:
            return False

    def clear_field(self):
        self.is_element_present()
        self.find_element().send_keys(Keys.CONTROL + "a")
        self.find_element().send_keys(Keys.DELETE)

    def find_elements(self):
        self.is_element_present()
        return DriverManager.get_driver().find_elements(self.__locator_type, self.__locator)

    def find_element(self):
        self.is_element_present()
        return DriverManager.get_driver().find_element(self.__locator_type, self.__locator)

    def check_element_visibility(self):
        return WebDriverWait(DriverManager.get_driver(), DRIVER_WAIT_TIME).until(
            EC.visibility_of_element_located((self.__locator_type, self.__locator)))

    def is_element_present(self):
        try:
            self.check_element_visibility()
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self):
        try:
            WebDriverWait(DriverManager.get_driver(), DRIVER_WAIT_TIME).until_not(
                EC.visibility_of_element_located((self.__locator_type, self.__locator)))
        except TimeoutException:
            return False
        return True

    @reuse
    def click(self):
        try:
            self.check_element_visibility()
            WebDriverWait(DriverManager.get_driver(), DRIVER_WAIT_TIME).until(
                EC.element_to_be_clickable((self.__locator_type, self.__locator)))
            self.find_element().click()
        except TimeoutException:
            return False
        except StaleElementReferenceException:
            self.find_element().click()
        return True

    @reuse
    def click_simple(self):
        try:
            self.check_element_visibility()
            self.find_element().click()
        except TimeoutException:
            return False
        return True

    def get_value(self):
        return self.find_element().get_attribute('value')

    def send_keys(self, keys):
        try:
            self.is_element_present()
            self.find_element().send_keys(keys)
            value = self.get_value()
            if value != keys:
                for _ in range(REUSE_NUMBER):
                    time.sleep(1)
                    self.check_element_visibility()
                    self.find_element().send_keys(keys)
                    value = self.get_value()
                    if value == keys:
                        break
        except TimeoutException:
            return False
        return True

    def send_simply(self, keys):
        try:
            self.check_element_visibility()
            self.find_element().send_keys(keys)
        except TimeoutException:
            return False
        return True
