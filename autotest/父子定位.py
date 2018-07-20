#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 11:47
# @Author  : zhangxingchen
# @Site    : 
# @File    : 父子定位.py
# @Software: PyCharm
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('F:\\python100\\autotest\\parent.html')

#串联查找
t1 = driver.find_element_by_id('B').find_element_by_tag_name('div').text
print(t1)

#xpath
#
t2 = driver.find_element_by_xpath("//div[@id='B']/div").text
#
print(t2)
# #css selector
#
t3 = driver.find_element_by_css_selector("#B").text
print(t3)