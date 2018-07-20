#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 14:16
# @Author  : zhangxingchen
# @Site    : 
# @File    : 遍历目录文件.py
# @Software: PyCharm

import os

path = 'F:\python100'

# dirpath = os.listdir(path)
#
# for i in dirpath:
#     print(i)
# list1= [i for i in os.listdir('.') if os.path.isdir(i)]
# print(list1)


for root, dirs, files in os.walk(path):
    # for f in files:
    #     print(os.path.join(root,f))
    print(root)
    print(dirs)
    print(files)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    for d in dirs:
        print(os.path.join(root,d))
    # print(root)
    # print(dirs)
    # print(files)
