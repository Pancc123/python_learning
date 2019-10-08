# -*- coding:utf-8 -*-


class read_txt:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):  # 读取列表返回整个文件对象组成的超大字符串
        with open(self.file_name, 'r') as objects:
            contents = objects.read()
            return contents

    def read_file2(self):  # 读取文件返回以每一行字符串组成的列表
        with open(self.file_name, 'r') as objects:
            data = objects.readlines()
            return data

    def read_file3(self):  # 读取文件单行读取
        with open(self.file_name, 'r') as objects:
            line = objects.readline()
            return line


