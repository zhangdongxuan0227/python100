#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 10:56
# @Author  : zhangxingchen
# @Site    : 
# @File    : enco.py
# @Software: PyCharm

import msvcrt  # 用于getch()

while True:

    print("请输入：")

    ch = msvcrt.getch()  # 键盘输入的是bytes

    print("%d" % (ch[0]))
    print(ch)
    print(ch.decode(encoding="utf-8"))
