# -*- coding:utf-8 -*-
import random


# 给出指定位数的数字字符串
def get_randomStr(number):
    data = ''
    for i in range(number):
        data = data + str(random.randint(0,9))
    print(data)
    return data


# get_randomStr(5)
