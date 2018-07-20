#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 13:53
# @Author  : zhangxingchen
# @Site    : 
# @File    : 九宫格.py
# @Software: PyCharm

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '4.4.2',
    'appPackage': 'com.jingjinsuo.jjs',
    'appActivity': 'com.tencent.mobileqq.activity.SplashActivity',
    'noReset': "true"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

sleep(5)



# 手势密码 封装： 九宫格（012；345；678）手势为：1478
def gesturepassword(self):
    list_pwd = self.driver.find_elements_by_class_name("android.widget.ImageView")
    TouchAction(self.driver).press(list_pwd[1]).move_to(list_pwd[1]).move_to(list_pwd[4]).wait(100).move_to(
        list_pwd[7]).wait(100).move_to(list_pwd[8]).release().perform()
    sleep(1)
    print("输入手势密码")
    # 如果为新注册，或者修改手势密码的时候，需要输入两次手势密码，如果只是登录的话就是一次
    try:
        ele = self.driver.find_element_by_name("请再绘制手势密码")
        list_pwd = self.driver.find_elements_by_class_name("android.widget.ImageView")
        TouchAction(self.driver).press(list_pwd[1]).move_to(list_pwd[1]).move_to(list_pwd[4]).wait(100).move_to(
            list_pwd[7]).wait(100).move_to(list_pwd[8]).release().perform()
    except Exception:
        pass
