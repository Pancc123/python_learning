# -*- coding : utf-8 -*-
from txt_rw import Rw_txt
import os,re

file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_path = os.path.join(file_path1, r'test_files\test.txt')
t = Rw_txt(file_path).read_file()
# print(t)
data = re.findall('"accountId":"(.+?)"',t)
print(data)
data1 = re.search('"accountId":"(.+?)"',t).group()
print(data1)
print(type(data1))