import os

from selenium.webdriver.common.by import By
from data.strings import CapabilitiesStrings as Capabilities


# Here can specify locator by current OS (@AndroidFindBy and @iOSFindBy for poor :D)
class AboutLocators:
    locator = (By.ID, "android_id") if os.getenv('os') == Capabilities.android else (By.ID, "ios_id")
    locator_xpath = (By.XPATH, "android_xpath") if os.getenv('os') == Capabilities.android else (By.XPATH, "ios_xpath")

