# -*- coding=utf-8 -*
# @Time :  2021-5-18 16:50
# @Author : ChengCheng Pan
import unittest
import paramunittest
import time


# 方法一：字典参数化
# @paramunittest.parametrized(
# {"user": "admin", "psw": "123", "result": "true"},
# {"user": "admin1", "psw": "1234", "result": "true"},
# {"user": "admin2", "psw": "1234", "result": "true"},
# {"user": "admin3", "psw": "1234", "result": "true"},
# {"user": "admin4", "psw": "1234", "result": "true"},
# {"user": "admin5", "psw": "1234", "result": "true"},
# {"user": "admin6", "psw": "1234", "result": "true"},
# {"user": "admin7", "psw": "1234", "result": "true"},
# {"user": "admin8", "psw": "1234", "result": "true"},
# {"user": "admin9", "psw": "1234", "result": "true"},
# {"user": "admin10", "psw": "1234", "result": "true"},
# {"user": "admin11", "psw": "1234", "result": "true"},
# )


# 元组参数化
@paramunittest.parametrized(
("admin", "123", "true"),
("admin1", "123", "true"),
("admin2", "123", "true"),
("admin3", "123", "true"),
("admin4", "123", "true"),
("admin5", "123", "true"),
("admin6", "123", "true"),
("admin7", "123", "true"),
("admin8", "123", "true"),
("admin9", "123", "true"),
("admin10", "123", "true"),
("admin11", "123", "true"),
("admin12", "123", "true")
)
class TestDemo(unittest.TestCase):
    def setParameters(self, user, psw, result):
        # '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.user = user
        self.user = psw
        self.result = result

    def testcase(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.user)
        print("期望结果：%s " % self.result)
        time.sleep(0.5)
        self.assertTrue(self.result == "true")


if __name__ == "__main__":
    unittest.main(verbosity=2)