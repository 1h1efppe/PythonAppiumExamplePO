import logging
import os
import subprocess
import pytest

from appium.webdriver.appium_service import AppiumService
from py._xmlgen import html
from datetime import datetime
from appium import webdriver
from selenium.common.exceptions import WebDriverException

from data.driver_data import GeneralData
from data.driver_data import AndroidDriverData
from data.driver_data import IOSDriverData


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(3, html.th('Timestamp', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(3, html.td(datetime.now(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.timestamp = str(item.function.__doc__)


# Get command line arguments for platform and OS version
def pytest_addoption(parser):
    parser.addoption('--os', action='store', default='android', help='target OS')
    parser.addoption('--os_version', action='store', default='10', help='select os Version')


def pytest_configure(config):
    os.environ["os"] = config.getoption('os')
    os.environ["os_version"] = config.getoption('os_version')


# Init driver
@pytest.fixture(scope='function')
def driver():
    logging.info('Preparing')
    appium_service = AppiumService()
    try:
        appium_service.start()
        logging.info('Starting Appium Server')
    except Exception as e:
        logging.error('Could not start Appium Server')
        logging.error(e)

    caps = {}
    logging.info('Starting driver and setting capabilities...')
    if os.getenv('os').lower() == 'android':
        caps = AndroidDriverData().android_caps('Android', os.getenv('os_version'))
        logging.info('Android capabilities is set to: ')
        for keys, values in caps.items():
            logging.info('{} : {}'.format(keys, str(values)))

    elif os.getenv('os').lower() == 'ios':
        caps = IOSDriverData().ios_caps('iOS', os.getenv('os_version'))
        logging.info('iOS capabilities is set to: ')
        for keys, values in caps.items():
            logging.info('{} : {}'.format(keys, str(values)))
    else:
        logging.error('{} is incorrect OS version'.format(os.getenv('os_version')))
    driver = webdriver.Remote(GeneralData.APPIUM_LOCAL_HOST_URL, desired_capabilities=caps)
    if driver:
        logging.info('Driver is ready')
    else:
        logging.error('WebDriver exception')
        raise WebDriverException

    yield driver
    logging.info('Quiting browser')
    try:
        logging.info('Trying to stop appium server')
        appium_service.stop()
    except Exception as e:
        logging.error('Error: '.format(e))
        logging.info('Killing appium instance')
        subprocess.run('killall node')
