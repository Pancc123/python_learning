# -*- coding:utf-8 -*-
import re
from collections import Counter


# 截取文档内容（2个参数，合并成一个字符串），返回字符串列表
def truncate_doc(file_name):
    L = []
    with open(file_name, 'r',encoding='utf-8')as f:
         # data = f.read()
        data = f.readlines()
        print(data)
        for line in data:
            t = re.findall(r'\d\.\d\.\d', line)
            if t:
                m = re.findall(r'\d{16}', line)
                if m:
                    n = m[0]+':'+t[0]
                    L.append(n)
    return L


# 去重，返回新列表
def distinct(m):
    m = list(set(m))
    return m
    # print(list2)


# 匹配元素，返回新列表
def match_list(list_name):
    list2 = []
    for row in list_name:
        t1 = re.findall(r'\d\.\d\.\d', row)
        t2 = "".join(t1)
        list2.append(t2)
    return list2


# 字典方式计数
def count_element(list_name):
    # print('total device: ' + str(len(list_name)))
    count = {}
    for item in list_name:
        # 返回指定键的值，如果值不在字典中返回default值
        count[item] = count.get(item, 0) + 1
    # print(count)
    return count
# 计数器方式统计列表内各个元素的数量
'''
def count_element(list_name):
  count = Counter(list_name)
  print(count)
  print(type(count))'''


# 展示各个版本的数量
def show_ver_num(dic):
    # 遍历字典，返回元组
    '''for item in dic1.items():
        print(item)'''
    # 遍历key值
    for key in dic.keys():
        print(key + ':   ' + str(dic[key]))


file_name = 'service.log'
list1 = truncate_doc(file_name)
# print(len(list1))
list3 = distinct(list1)
# print(len(list2))
list4 = match_list(list3)
ct = count_element(list4)
show_ver_num(ct)
