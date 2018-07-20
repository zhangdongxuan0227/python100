#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 10:15
# @Author  : zhangxingchen
# @Site    : 
# @File    : 星号密码.py
# @Software: PyCharm
import msvcrt


def pwd_input():
    chars = []
    while True:
        try:
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:
            return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")
        if newChar in '\r\n':  # 如果是换行，则输入结束
            break
        elif newChar == '\b':  # 如果是退格，则删除密码末尾一位并且删除一个星号
            if chars:
                del chars[-1]
                msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格
                msvcrt.putch(' '.encode(encoding='utf-8'))  # 输出一个空格覆盖原来的星号
                msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格准备接受新的输入
        else:
            chars.append(newChar)
            msvcrt.putch('*'.encode(encoding='utf-8'))  # 显示为星号
    return (''.join(chars))


print("请输入密码：")
pwd = pwd_input()
print("\n密码是：{0}".format(pwd))
input("按回车键退出")