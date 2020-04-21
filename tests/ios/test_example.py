import allure

from screens.example import ExampleScreen


@allure.testcase('Test activation with Install Referrer from ADB command')
def test_test(driver):
    assert ExampleScreen(driver).do_something()
