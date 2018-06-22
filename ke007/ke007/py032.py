# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:
import unittest


# 1.测试类，继承TestCase
# 2。测试类，没有init初始化
# 3。每一条测试用例，必须以test开头
# 4.测试用例的通过标准：1）如果有断言，那么断言结果为真，那么用例通过
#                   2）如果没有断言，那么程序执行必须没有异常
# 5.测试用例的执行默认顺序ASCII
# 6.setUP与tearDown，前置条件和后置条件，这两个方法，每次执行测试用例的时候都会执行，每一条用例，都是同样都前置和后置条件
# 7.前置条件和后置条件，只执行一次，使用setUpClass和tearDownClass，这两个方法，都要配合装饰器classmethod使用
# 8。同时存在setUP、setUpClass、tearDown、tearDownClass
# 先执行setUpClass和tearDownClass，带class的两个方法，是类级的。cls和self是一样的用法。
# 9。跳过或者条件执行测试用例
# 10。一条测试用例，可以有多个断言，只要有一个不通过，视为用例不通过

class MyTest(unittest.TestCase):
    m = 1

    def setUp(self):
        self.a = 1
        print(self.a)

    @classmethod
    def setUpClass(cls):
        print("这是一个前置条件！")

    def test_01_Add(self):
        b = 3
        c = 'aaa'
        self.a = self.a + b
        print(self.a)

    # c+1
    # self.assertEqual(a+b,4)

    def test_02_AAA(self):
        c = 3
        self.a = c - self.a
        print(self.a)

    # @unittest.skip("跳过测试用例")  # 跳过测试用例的装饰器，括号里面用来写描述的，描述可写可不写
    # @unittest.skip
    def test_03(self):
        print("这是第三条测试用例")

    @unittest.skipIf(m == 1, "m=1的时候跳过")  # 指定条件满足，跳过执行测试用例，第一个参数添加表达式，第二个参数填写描述
    # @unittest.skipUnless(m==1,"m=1的时候跳过")      # 指定条件不满足的时候，跳过执行测试用例
    def test_04(self):
        print("这是第四条测试用例")

    def tearDown(self):
        self.a = 1
        print('---------')

    @classmethod
    def tearDownClass(cls):
        print("这是一个后置条件")


if __name__ == '__main__':
    # unittest.main()
    casetest = unittest.TestSuite()
    casetest.addTest(MyTest("test_01_Add"))
    # casetest.addTests()  批量添加测试用例
    print(casetest)
    print(casetest.countTestCases())
    # dis = unittest.defaultTestLoader.discover(start_dir=, pattern="test*.py")
    # start_dir 填写路径，用来查找测试用例
    # pattern 匹配规格，测试用例py文件的匹配规则
    # discover 匹配出来所有的测试用例，dis就是所有测试用例的集合
    # discover和suite，两个可以一起使用，也可以单独使用，不存在必要的因果关系
    runner = unittest.TextTestRunner()
    runner.run(casetest)
