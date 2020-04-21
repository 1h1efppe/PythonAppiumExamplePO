import logging


# A little bit reworked logging for my needs to fit better with Selenium/Appium
class LoggingHelper:
    def info(self, message):
        logging.info(message)

    def error(self, message):
        logging.error(message)

    def locator_found_message(self, locator):
        return 'Element {} found'.format(locator)

    def locator_check_message(self, locator):
        return 'Checking for {} element'.format(locator)

    def locator_not_found(self, locator):
        return 'Element {} not found'.format(locator)

    def clicking_locator(self, locator):
        return 'Clicking {} element'.format(locator)

    def weaiting_for_click(self, locator):
        'Waiting for {} element to click it'.format(locator)

    def sending_text_to_element(self, text, locator):
        'Sending {} to {} element'.format(text, locator)

    def getting_text_from_element(self, locator):
        'Getting text from {} element'.format(locator)

    def text_of_locator(self, locator, element):
        'Text of {} is {}'.format(locator, element.text)