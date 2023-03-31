# -*- coding:utf-8 -*-
from time import sleep
import pytest
from appium import webdriver
from hamcrest import assert_that, equal_to, close_to, contains_string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "appium:deviceName": "AKC7N18623004548",
            # "appium:appPackage": "com.ss.android.article.lite",
            # "appium:appActivity": ".activity.SplashActivity",
            "appium:appPackage": "com.xueqiu.android",
            "appium:appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "unicodeKeyBoard": True,  #默认英文输入，若想输入中文，需加入此参数
            "resetKeyBoard": True,  #默认英文输入，若想输入中文，需加入此参数
            "dontStopAppOnReset": True,  # 首次启动时，不停止app(可以调试或运行时提示运行速度)
            "skipDeviceInitialization": True  # 跳过安装，权限设置等操作
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        # # self.driver.back()
        #         # self.driver.back()
        #         # self.driver.back()返回上一页
        self.driver.find_element(By.ID,'com.xueqiu.android:id/action_close').click()

        pass
    def test_search(self):
        self.driver.find_element(By.ID,'com.ss.android.article.lite:id/blf').click()
        #self.driver.find_element(By.ID, 'com.ss.android.article.lite:id/bld').click()
        self.driver.find_element(By.ID, 'com.ss.android.article.lite:id/da').send_keys("台湾地震")

        sleep(3)
        self.driver.find_element(By.XPATH, '//android.widget.RelativeLayout[@content-desc="台湾地震，链接,"]').click()
    def test_attr(self):
        element = self.driver.find_element(By.ID, 'com.ss.android.article.lite:id/bld')
        print(element.is_enabled()) #判断搜索框是否可用
        print(element.text) #查看搜索框name属性值
        print(element.location) #打印搜索框这个元素的左上角坐标
        print(element.size) #打印搜索框这个元素的宽高
        search_enabled = element.is_enabled()
        if search_enabled == True:
            element.click()
            shuru_element = self.driver.find_element(By.ID, 'com.ss.android.article.lite:id/da').send_keys("台湾地震")
            #shuru_element.is_displayed() #输入的内容是否可见
            #另一种方法判断输入内容是否可见，打印出的是true为字符串
            #print(shuru_element.get_attribute("displayed"))
            element_display = shuru_element.get_attribute("displayed") #打印出的是True，为布尔值
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_get_current(self):
        # self.driver.find_element(By.ID,"com.xueqiu.android:id/home_search").click()
        # sleep(3)
        # self.driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # sleep(5)
        # self.driver.find_element(By.XPATH,"//*[@text='BABA']").click()
        # #先判断页面中是否此元素，若有此元素是否为可点击状态
        # locator = (By.XPATH, "//*[@text='09988']/../..//*[@resource-id='com.xueqiu.android:id/current_price_dtv']")
        # # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # # ele = self.driver.find_element(*locator) #*locator是两个变量。By.XPATH ,"username",即：driver.find_element(By.XPATH,"username")
        # #使用lambda表达式
        # ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        # print(float(ele.text))
        # #assert float(ele.text) < 200
        # assert_that(float(ele.text), close_to(75, 75*0.1)) #期望值为75，上下浮动范围(67.5-82.5)
        @pytest.mark.parametrize('searchkey,type',[
            ('阿里巴巴','BABA'),
            ('小米','01810')
        ])
        self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("searchkey")
        sleep(5)
        self.driver.find_element(By.XPATH, "//*[@text='{type}']").click()
        locator = (By.XPATH, "//*[@text='09988']/../..//*[@resource-id='com.xueqiu.android:id/current_price_dtv']")
        ele = self.driver.find_element(*locator)
        print(float(ele.text))
        assert float(ele.text) < 200


    #获取属性值get_attribute
    def test_get_attr(self):
        search_ele = self.driver.find_element(By.ID,"com.xueqiu.android:id/home_search")
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("bounds"))
        assert 'search' in search_ele.get_attribute("resource-id")
    #断言
    def test_assert(self):
        a = 10
        b = 20
        #assert a > b #执行到错误的断言时就不继续下面的执行
        assert 'h' in 'this'

    def test_hamrest(self):
        #assert_that(10,equal_to(9),'这是一个提示') #equal_to等于
        assert_that(9,close_to(10,2)) #10为期望值，上下浮动2
        assert_that("contains some string", contains_string("string")) #contains_string()包含字符串