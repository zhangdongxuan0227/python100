#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 15:55
# @Author  : zhangxingchen
# @Site    : 
# @File    : frame.py
# @Software: PyCharm

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('F:\\python100\\autotest\\frame.html')
# #不推荐
# #driver.switch_to_frame()
# driver.switch_to.frame('frame1')
#
# driver.switch_to.default_content()

def filternum(listnum):
    jishu = []
    oushu = []
    for i in listnum:
        if i % 2 == 0:
            oushu.append(i)
        else:
            jishu.append(i)
    if len(jishu) == len(listnum) - 1:
        return oushu[0]
    else:
        return jishu[0]


list1 = [160, 20, 21, 56, 60, 88]

print(filternum(list1))
