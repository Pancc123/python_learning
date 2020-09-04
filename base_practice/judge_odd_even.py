# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数

num = int(input("输入一个数字: "))
if (num % 2) == 0:
   print("%d是偶数"%(num))
else:
   print("%d是奇数"%(num))
