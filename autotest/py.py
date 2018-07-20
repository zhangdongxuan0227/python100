#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 21:34
# @Author  : zhangxingchen
# @Site    : 
# @File    : py.py
# @Software: PyCharm

from pymouse import PyMouse
import win32api

import win32con

win32api.MessageBox(win32con.NULL, '我的第一个pywin32窗口！', 'Hello', win32con.MB_OK)