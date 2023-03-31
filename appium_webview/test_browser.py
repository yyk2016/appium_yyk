# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver


class TestBrowser():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "AKC7N18623004548",
            "browserName": "browser",
            "noReset": True,
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True
            #"chromedriverExecutable":"E:\Appium\Appium1.2\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        sleep(3)
        #self.driver.implicitly_wait(5)

    def teardown(self):
        #self.driver.quit()
        pass
    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(3)