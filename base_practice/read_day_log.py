# -*- coding; utf-8 -*-
import os


def get_log(logic_addr, list2=[]):
    list1 = os.listdir(os.getcwd())
    for file in list1:
        if logic_addr in file:
            list2 = list2.append(file)
