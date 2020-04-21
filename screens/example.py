import allure

from screens.base import BaseScreen as Base
from utility.logs_methods import LoggingHelper as Logs
from locators.about import AboutLocators
from utility.shell_runner import ShellRunner


# If command line argument of driver was Android, for example, in this case our driver instance will
# be with android capabilities AND our locator will be for Android, so if the app have similar screens
# we can use same methods for both platforms
class ExampleScreen(Base):
    logs = Logs()

    @allure.step('your allure step description')
    def do_something(self):
        Logs.info(self.logs, 'Checking that element is on page')
        return Base(self.driver).check_element_is_on_page(*AboutLocators.locator)

    @allure.step('Preparation steps')
    def prepare_app(self):
        Logs.info(self.logs, 'Preparing the app')
        ShellRunner().run_command("adb devices")
