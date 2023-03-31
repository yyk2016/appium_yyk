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
            "unicodeKeyBoard": True,  # Ĭ��Ӣ�����룬�����������ģ������˲���
            "resetKeyBoard": True,  # Ĭ��Ӣ�����룬�����������ģ������˲���
            "dontStopAppOnReset": True,  # �״�����ʱ����ֹͣapp(���Ե��Ի�����ʱ��ʾ�����ٶ�)
            "skipDeviceInitialization": True  # ������װ��Ȩ�����õȲ���
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        pass
    def test_touchaction(self):
        action = TouchAction(self.driver)
        #����㷽ʽ������xy��������ڵ�λ�ã��ƶ�����һ��xy��������ڵ�λ�ã���wait()��ֹ������̫��
        #action.press(x=542,y=1925).wait(400).move_to(x=500,y=917).release().perform()
        #�豸�䣬�������ܻ�䣬����һ�ֲ������,�豸�Ŀ��
        print(self.driver.get_window_rect()) #��ȡ�豸�Ŀ�͸�
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height* 4/5)
        y_end = int(height* 1/5)
        action.press(x=x1, y=y_start).wait(400).move_to(x=x1, y=y_end).release().perform()

    #���ƽ���
    def test_touchaction_unlock(self):
        action = TouchAction(self.driver)
        action.press(x=243,y=395).wati(200).move_to(x=721,y=378).wait(200).move_to(x=1190,y=364).wait(200).move_to(x=1202,y=859).wait(200)\
        .move_to(x=1195,y=1339).release().perform()