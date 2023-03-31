# -*- coding: utf-8 -*-
import time
from time import sleep
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import re

# def getContent():


random.seed(datetime.now())

# 复用浏览器，不用每次执行打开新的窗口
opt = Options()
# 和浏览器打开的调试端口进行通信
# 浏览器要使用 chrome --remote-debugging-port=9222 开启调试
opt.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=opt)
wait = WebDriverWait(driver, 5)

driver.get("https://www.xiaohongshu.com/explore")

sleep(random.uniform(5,9))
# try:
ActionChains(driver).move_by_offset(200, 100).click().perform()

def saveText(list):
    print(str(list).encode('utf8'))
    with open('xhs.txt','a+',encoding='utf8') as f:
        f.writelines(','.join(list).replace('\n','')+'\n')

while 1:
    for i in range(1,7):
        result = []
        blog_ele = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/section[{}]/a[2]'.format(i))
        blog_ele.click()
        sleep(random.uniform(2,4))
        title = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]').text
        result.append(str(title).strip().replace(',',''))
        content = driver.find_elements(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[2]/div[2]/div[1]')
        for c in content:
            result.append(str(c.text).strip().replace(',',''))
        date = driver.find_element(By.CLASS_NAME,'date')
        result.append(date.text.strip())
        print(str(date.text).strip())

        like = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/span[2]')
        print('点赞数量：',like.text)
        collect = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[2]/span')
        print('收藏数量：',collect.text)
        comment = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[3]/span')
        print('评论数量：',comment.text)
        result.extend([like.text,collect.text,comment.text])

        #获取网页源码
        html_source = driver.page_source
        pattern1 = '''background-image: url\((.+?)\)'''
        items = re.findall(pattern1,html_source)
        temItems = []
        for item in items:
            temItems.append(str(item).replace('&quot;',''))
        result.extend(temItems)
        saveText(result)

        back_ele = driver.find_element(By.CLASS_NAME,'close')
        back_ele.click()
        sleep(random.uniform(2,4))
    reload_ele = driver.find_element(By.CLASS_NAME, 'reload')
    reload_ele.click()
    sleep(random.uniform(3,5))


# print(close_login_ele)
# close_login_ele.click()
# except:
#     print('不能关闭')
