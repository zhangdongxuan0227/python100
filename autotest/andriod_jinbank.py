#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 19:10
# @Author  : zhangxingchen
# @Site    : 
# @File    : andriod_jinbank.py
# @Software: PyCharm


from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

'''
启动京金所app
'''

desired_caps = {
    'platformName': 'Android',
    'deviceName': '69P0216',  # HUAWEI
    'platformVersion': '5.0.2',
    # apk包名
    'appPackage': 'com.jingjinsuo.jjs',
    # apk的launcherActivity
    'appActivity': 'com.jingjinsuo.jjs.activities.WelcomeActivity'
}

# desired_caps['platformName'] ='Android'
#
# desired_caps['platformVersion'] ='6.0.1'
#
# desired_caps['deviceName'] ='e0bbc8b7'
#
# desired_caps['appPackage'] ='com.ximalaya.ting.android'
#
# desired_caps['appActivity'] ='com.ximalaya.ting.android.host.activity.WelComeActivity'
#
# desired_caps["unicodeKeyboard"] ="True"
#
# desired_caps["resetKeyboard"] ="True"

desired_caps = {
    'platformName': 'Android',
    'deviceName': '69P0216',  # HUAWEI
    'platformVersion': '5.0.2',
    # apk包名
    'appPackage': 'com.jingjinsuo.jjs',
    # apk的launcherActivity
    'appActivity': 'com.jingjinsuo.jjs.activities.WelcomeActivity'
}

remote_ip = 'http://127.0.0.1:4723/wd/hub'


class jinbank_app(object):

    def login(self, ip, caps):
        self.driver = webdriver.Remote(ip, caps)
        print("启动成功")
        return

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


if __name__ == '__main__':
    lan = jinbank_app()
    lan.login(remote_ip, desired_caps)
