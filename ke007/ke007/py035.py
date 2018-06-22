# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:
import unittest


class Mytest(unittest.TestCase):

    def test_01(self):
        a = 1
        b = 2
        c = 3
        # 常用的断言
        # 一条测试用例，可以有多个断言，只要有一个不通过，视为用例不通过
        self.assertEqual()  # 相等
        self.assertNotEqual()
        self.assertFalse()  # 为假，布尔值
        self.assertTrue()
        self.assertIn()  # 包含
        self.assertNotIn()
        self.assertIs()  # XXX是XXXX，添加表达式
        self.assertIsNone()  # 是空
        self.assertTupleEqual()
        self.assertListEqual()
        self.assertDictEqual()
        self.assertSetEqual()  # set python里面的一种数据结构，集合
        self.assertIsInstance()
        self.assertNotIsInstance()
    # ……
