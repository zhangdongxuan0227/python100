#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 12:07
# @Author  : zhangxingchen
# @Site    : 
# @File    : no_repeat.py
# @Software: PyCharm

import os, sys

for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if (x != y) and (y != z) and (z != x):

                print("%d%d%d" % (x, y, z), end="|")
                print("{0}{1}{2}".format(x, y, z), end="|")

print(os.getenv("JAVA_HOME"))
