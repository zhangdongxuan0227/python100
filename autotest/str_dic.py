#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 21:24
# @Author  : zhangxingchen
# @Site    : 
# @File    : str_dic.py
# @Software: PyCharm

str = "k:1|k1:2|k2:3|k3:4"

str1 = str.split("|")
print(str1)

dic={}
for x in str1:
    k = x.split(":")
    print(k)
    dic[k[0]]=k[1]


print(dic)

d = {"name":"zxc","age":123,"class":2}

print(d[0])