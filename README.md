<h1> Simple Python and Appium PageObject (ScreenObject) example </h1>

![](https://github.com/betaraybill/PythonExamplePO/blob/media/phones.png?raw=true)

## Description

* Fairly simple PageObject pattern. Include
  - PyTest
  - Allure reports
  - Logging
* Easy to maintain, no unnecessary 3-rd party packages/wrappers
* Just clone it and put your app/locators/logic
  


## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Pipenv](https://github.com/pypa/pipenv), [Appium](https://appium.io), and Android/iOS simulator or real device.
```bash
# Clone this repository
$ git clone https://github.com/betaraybill/PythonExamplePO.git

# Go into the repository
$ cd PythonExamplePO

# Install dependencies
$ pipenv install

# After that, change the code, according to your app needs, and run:

# android
$ pipenv run py.test -s --os=android --os_version=10 test_test.py

# ios
$ pipenv run py.test -s --os=android --os_version=10 test_test.py


# If you want to have allure report and logs
$ pipenv run py.test --log-cli-level=INFO -s --alluredir=/path/to/desired/alluredir --os=android --os_version=10 test_test.py

# To get allure report
$ allure generate --clean allure/ -o allure/reports && allure open allure/reports


# If for some reason you don't like Allure, you can use Pytest built-in reports, to do this - add --html=report.html
pipenv run py.test --log-cli-level=INFO -s --reruns 2 --html=report.html --os=android --os_version=10 test_test.py

# And finally, if you have flaky tests, you can run tests with rerun option. In this case, test will run N times if it fails. Usually, 3 is fair enough.
pipenv run py.test --log-cli-level=INFO -s --reruns 2 --html=report.html --reruns 5 --os=android --os_version=10 test_test.py 
```



## Contact me

Feel free to make any pull-request if you have something to add or change.
Also, you can contact me by email: raijinthegodofthunder@gmail.com, in case if you have something to ask or tell me.


## Header image by
<a href="https://www.vecteezy.com/free-vector/smartphone">Smartphone Vectors by Vecteezy</a>
