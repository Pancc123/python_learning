# -*- coding=utf-8 -*
# @Time :  2021-5-11 16:11
# @Author : ChengCheng Pan

import unittest
from ddt import ddt,data,unpack

'''
@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        print('this is the setUp')

    @data([1,2,3])
    def test_1(self,value):
        print(value)

    @data([3,2,1],[5,3,2],[10,4,6])
    @unpack
    def test_minus(self,a,b,expected):
        actual = int(a) - int(b)
        expected = int(expected)
        self.assertEqual(actual, expected)

    @data([2,3],[4,5])  # test_compare的测试结果是fail的，由于没有加@unpack, 虽然还是会被理解成2组测试数据，但是[2,3]作为一个整体被传给了a, 因为b就没有值传入
    def test_compare(self,a,b):
        self.assertEqual(a,b)

    def tearDown(self):
        print('this is tearDown')
'''


@ddt
class MyTest(unittest.TestCase):

    @data((8, 6), (4, 0), (15, 6))
    @unpack
    def test_tuples(self, first, second):
        self.assertTrue(first > second)

    @data([30, 29], [40, 30], [5, 3])
    @unpack
    def test_list(self, first, second):
        self.assertTrue(first > second)

    @data({'first': 1, 'second': 3, 'third': 5},
          {'first': 4, 'second': 7, 'third': 8})
    @unpack
    def test_dicts(self, first, second, third):
        self.assertTrue(first < second < third)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # unittest.main()
