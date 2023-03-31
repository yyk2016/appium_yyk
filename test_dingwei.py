#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='6.0.1'
# desired_caps['deviceName']='127.0.0.1:7555'
# desired_caps['appPackage']='com.android.browser'
# desired_caps['appActivity']='com.android.browser.BrowserActivity'


desired_caps={
  "platformName": "android",
  "appium:deviceName": "AKC7N18623004548",
  "appium:appPackage": "com.ss.android.article.lite",
  "appium:appActivity": ".activity.SplashActivity",
  #"appium:appPackage": "com.UCMobile",
  #"appium:appActivity": ".main.UCMobile",
  "noReset": True,
  "dontStopAppOnReset": True, #首次启动时，不停止app(可以调试或运行时提示运行速度)
  "skipDeviceInitialization": True #跳过安装，权限设置等操作
}
#初始化driver，可以和手机进行通讯
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)
# el22 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.RelativeLayout[@content-desc=\"头条\"]/android.widget.ImageView")
# el22.click()
# el23 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.RelativeLayout[@content-desc=\"小说\"]/android.widget.ImageView")
# el23.click()

#元素定位方法
driver.find_element(By.ID, 'com.ss.android.article.lite:id/bld').click()
driver.find_element(By.ID, 'com.ss.android.article.lite:id/da').send_keys("台湾地震")
sleep(3)
driver.find_element(By.XPATH,'//android.widget.RelativeLayout[@content-desc="台湾地震，链接,"]').click()
#返回上一页
driver.back()
driver.back()
driver.back()
