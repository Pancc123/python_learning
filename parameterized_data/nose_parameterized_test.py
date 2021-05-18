# -*- coding=utf-8 -*
# @Time :  2021-5-18 17:04
# @Author : ChengCheng Pan
import unittest
# from nose_parameterized import parameterized
from parameterized import parameterized


class TestAdd(unittest.TestCase):

    @parameterized.expand([
        ("01",1,2,3),
        ("02",2,2,4),
        ("03",0,4,4),
    ])
    def test(self, name, a, b, c):
        self.assertEqual(a+b,c)


if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
这里的verbosity是一个选项,表示测试结果的信息复杂度，有三个值
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.”  每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
并且 你在命令行里加入不同的参数可以起到一样的效果
加入 --quiet 参数 等效于 verbosity=0
加入--verbose参数等效于 verbosity=2
什么都不加就是 verbosity=1
"""