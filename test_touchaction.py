from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "appium:deviceName": "AKC7N18623004548",
            "appium:appPackage": "com.ss.android.article.lite",
            "appium:appActivity": ".activity.SplashActivity",
            "noReset": True,
            "unicodeKeyBoard": True,  # 默认英文输入，若想输入中文，需加入此参数
            "resetKeyBoard": True,  # 默认英文输入，若想输入中文，需加入此参数
            "dontStopAppOnReset": True,  # 首次启动时，不停止app(可以调试或运行时提示运行速度)
            "skipDeviceInitialization": True  # 跳过安装，权限设置等操作
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        pass
    def test_touchaction(self):
        action = TouchAction(self.driver)
        #坐标点方式：按下xy坐标点所在的位置，移动到另一个xy坐标点所在的位置，加wait()防止滑动的太快
        #action.press(x=542,y=1925).wait(400).move_to(x=500,y=917).release().perform()
        #设备变，坐标点可能会变，用另一种不变的量,设备的宽高
        print(self.driver.get_window_rect()) #获取设备的宽和高
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height* 4/5)
        y_end = int(height* 1/5)
        action.press(x=x1, y=y_start).wait(400).move_to(x=x1, y=y_end).release().perform()

    #手势解锁
    def test_touchaction_unlock(self):
        action = TouchAction(self.driver)
        action.press(x=243,y=395).wati(200).move_to(x=721,y=378).wait(200).move_to(x=1190,y=364).wait(200).move_to(x=1202,y=859).wait(200)\
        .move_to(x=1195,y=1339).release().perform()