import allure

from screens.example import ExampleScreen


# Setup and teardown specified in conftest.py file
@allure.testcase('Test activation with Install Referrer from ADB command')
def test_test(driver):
    ExampleScreen(driver).prepare_app()
    assert ExampleScreen(driver).do_something()
