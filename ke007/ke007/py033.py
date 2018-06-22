# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:
import unittest
from ke007.ke007.py032 import MyTest

# suite 使用的时候最好跟测试用例类分开文件
# 单个添加测试用例到测试套件
# 测试用例的执行顺序，可按照添加用例的顺序执行

if __name__ == '__main__':
    # unittest.main()
    casetest = unittest.TestSuite()
    casetest.addTest(MyTest("test_03"))
    casetest.addTest(MyTest("test_01_Add"))
    print(casetest)
    print(casetest.countTestCases())
    runner = unittest.TextTestRunner()
    runner.run(casetest)
