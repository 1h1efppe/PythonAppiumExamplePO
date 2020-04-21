from data.strings import CapabilitiesStrings as Capabilities
from data.strings import AndroidString as Android
from data.strings import IosStrings as Ios
from data.strings import ServerStrings as Server


# In this file we can prepare both our capabilities set to use them in our driver
class GeneralData:
    APPIUM_LOCAL_HOST_URL = Server.server_url


class AndroidDriverData:
    ANDROID_DEVICE_NAME = Android.device_name
    APP_PATH = Android.app_path
    APP_PACKAGE = Android.app_package
    APP_ACTIVITY = Android.app_activity
    AUTOMATION_NAME = Android.automation_name

    def android_caps(self, platform, version=Android.latest):
        desired_caps = {
            Capabilities.platform_name: platform,
            Capabilities.platform_version: version,
            Capabilities.device_name: self.ANDROID_DEVICE_NAME,
            Capabilities.app_package: self.APP_PACKAGE,
            Capabilities.app_activity: self.APP_ACTIVITY,
            Capabilities.clear_system_files: True,
            Capabilities.automation_name: self.AUTOMATION_NAME,
        }
        return desired_caps


class IOSDriverData:
    APP_PATH = Ios.app_path
    IOS_DEVICE_NAME = Ios.device_name
    AUTOMATION_NAME = Ios.automation_name

    def ios_caps(self, platform, version=Ios.latest):
        desired_caps = {
            Capabilities.platform_name: platform,
            Capabilities.platform_version: version,
            Capabilities.device_name: self.IOS_DEVICE_NAME,
            Capabilities.automation_name: self.AUTOMATION_NAME,
            Capabilities.app: self.APP_PATH
        }
        return desired_caps
