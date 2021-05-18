# -*- coding=utf-8 -*
# @Time :  2021-5-14 10:46
# @Author : ChengCheng Pan
import os

import os

pathlog = r"D:/"
files = os.listdir(pathlog)
for f in files:
    # print(f)
    if 'pm' in f and f.endswith('.csv'):
        print ("Found it! " + f)


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1] == '.jpeg':
            list_name.append(file_path)


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件