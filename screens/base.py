from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utility.logs_methods import LoggingHelper
from data.constants import TestConst as tc


# This is base screen with all mostly used methods, waits included
class BaseScreen:
    def __init__(self, driver):
        self.driver = driver

    logs = LoggingHelper()

    def check_element_is_on_page(self, locator):
        self.logs.info(self.logs.locator_check_message(locator))
        try:
            WebDriverWait(self.driver, tc.wait_time).until(ec.presence_of_element_located(locator))
            self.logs.info(self.logs.locator_found_message(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise

    def find_and_click_element(self, locator):
        self.logs.info(self.logs.locator_check_message(locator))
        try:
            element = WebDriverWait(self.driver, tc.wait_time).until(ec.presence_of_element_located(locator))
            self.logs.info(self.logs.clicking_locator(locator))
            element.click()
            return True
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise

    def wait_and_click_clickable_element(self, locator):
        self.logs.info(self.logs.weaiting_for_click(locator))
        try:
            element = WebDriverWait(self.driver, tc.wait_time).until(ec.element_to_be_clickable(locator))
            self.logs.info(self.logs.clicking_locator(locator))
            element.click()
            return True
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise

    def set_text(self, locator, text):
        try:
            element = WebDriverWait(self.driver, tc.wait_time).until(ec.presence_of_element_located(locator))
            self.logs.info(self.logs.sending_text_to_element(text, locator))
            element.set_value(text)
            return True
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise

    def get_text(self, locator):
        self.logs.info(self.logs.getting_text_from_element(locator))
        try:
            element = WebDriverWait(self.driver, tc.wait_time).until(ec.presence_of_element_located(locator))
            self.logs.info(self.logs.text_of_locator(locator, element))
            return element.text
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise
