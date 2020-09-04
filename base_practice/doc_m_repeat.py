#! -*- coding:utf-8 -*-
import re


empty_list = []
filename = 'C:\\Users\\dell\\Desktop\\Test_20130101'
with open(filename, 'r') as f:
    lines = f.readlines()
    tt = []
    for line in lines:
        t = re.findall(r'readTime=18/10/\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}', line)
        if t not in tt:
            tt.append(t)
            empty_list.append(line)

with open('C:\\Users\\dell\\Desktop\\Test_20130101.log','w') as f1:
    for i in empty_list:
        f1.write(i)
'''
#此方法会打乱列表原始的顺序       
{with open(filename,'r') as f:
   data = f.readlines()
    for line in data:
        empty_list.append(line)

    #data1 = list(set(data))
list_data=[]
for t in empty_list:
    if t not in list_data:
        list_data.append(t)

with open('C:\\Users\\dell\\Desktop\\Test_20130101.log','w') as f1:
    for i in list_data:
        f1.write(i)}
'''
# /d{1,2}:/d{1,2}:/d{1,2}