#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 15:05
# @Author  : zhangxingchen
# @Site    : 
# @File    : ke1.py
# @Software: PyCharm
import requests

# def getjiekuan():
#     url = "host/admin/menu_3310_251.html"
#     h = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
#         'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         'Referer': "http://182.92.96.122:8081/admin/manager_menu.action?actionId=3",
#         'Accept-Encoding': "gzip, deflate",
#         'Accept-Language': "zh-CN,zh;q=0.9",
#     }
#
#     res = requests.request("get", url, headers=h)
#     print(res.content.decode("utf-8"))

url = "http://182.92.96.122:8081/admin/menu_3310_251.html"
h = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://182.92.96.122:8081/admin/manager_menu.action?actionId=3",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
}

res = requests.request("GET", url, headers=h)
print(res.status_code)
print(res.content.decode("utf-8"))
