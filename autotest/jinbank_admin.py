#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 15:42
# @Author  : zhangxingchen
# @Site    : 
# @File    : jinbank_admin.py
# @Software: PyCharm
import requests

host = "http://182.92.96.122:8081"


def login(s, user, pwd):
    url = "host/admin/manager_login.action"

    h = {'Content-Type': "application/x-www-form-urlencoded",
         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
         'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
         'Accept-Encoding': "gzip, deflate",
         'Accept-Language': "zh-CN,zh;q=0.9",
         }
    payload = {"isVerify": '0',
               "act": 'signin',
               "userName": user,
               "password": pwd,
               "adminPath": 'jjswd',
               }
    # "isVerify=0&act=signin&userName=user&password=pwd&adminPath=jjswd"

    res = requests.request("POST", url, data=payload, headers=h)

    # print(res.status_code)
    #
    print(res.content.decode("utf-8"))
    return (res.content.decode('utf-8'))


def is_sucesslog(respond):
    if "系统管理登录" in respond:
        return False
    elif "京金所-验证环境" in respond:
        return True
    else:
        return False


def getjiekuan():
    url = "host/admin/menu_3310_251.html"
    h = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://182.92.96.122:8081/admin/manager_menu.action?actionId=3",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
    }

    res = requests.request("get", url, headers=h)
    print(res.content.decode("utf-8"))


if __name__ == '__main__':
    s = requests.session()
    a = login(s, "admin", "admin")
    result = is_sucesslog(a)
    print("测试结果：%s" % result)
