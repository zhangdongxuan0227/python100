#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 17:22
# @Author  : zhangxingchen
# @Site    : 
# @File    : 时间戳.py
# @Software: PyCharm

import time
import numpy as np

timestamplist = np.array([1531289307645,
                          1531293044606,
                          1531298119392,
                          1531298148210,
                          1531298753638,
                          1531298780289])

for i in range(len(timestamplist)):
    # timestamp转化为struct_time结构
    x = time.localtime(timestamplist[i]/1000)
    # 将struct_time按一定格式输出为string
    real_time = time.strftime('%Y-%m-%d %H:%M:%S', x)
    print(real_time)
