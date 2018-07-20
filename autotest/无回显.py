#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 20:14
# @Author  : zhangxingchen
# @Site    : 
# @File    : 无回显.py
# @Software: PyCharm

import getpass

name = input("输入你的名字：")
passwd = getpass.getpass("输入密码：")
print(name)
print(passwd)