# Helper classes with strings and variables for driver init


# This is not mandatory, but I prefer not to see any strings outside of values classes like this, but feel free to
# change structure whatever you like
class CapabilitiesStrings:
    android = 'android'
    ios = 'ios'
    platform_name = 'platformName'
    platform_version = 'platformVersion'
    device_name = 'deviceName'
    app_package = 'appPackage'
    app_activity = 'appActivity'
    automation_name = 'automationName'
    app = 'app'
    clear_system_files = 'clearSystemFiles'


class ServerStrings:
    server_url = 'http://localhost:4723/wd/hub'  # or your cloud appium server url


class AndroidString:
    device_name = 'Google Pixel 4'
    app_package = 'com.my.app'
    app_activity = 'com.my.app.ui.main.MainNavigationActivity'  # you need to have package and activity, to run the app
    app_path = '/Path/To/My/app.apk'
    latest = '10'
    clear_system_files = 'clearSystemFiles'
    automation_name = 'Appium'


class IosStrings:
    app_path = '/Path/To/My/app.app'
    device_name = 'iPhone 11'
    automation_name = 'XCUITest'
    latest = '13.4'
