# -*- coding:utf-8 -*-
import random,os


class Rw_txt:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):  # 读取列表返回整个文件对象组成的超大字符串
        with open(self.file_name, 'r',encoding='utf-8') as objects:
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

    def write_file(self, data):
        with open(self.file_name, 'w') as objects:
            objects.write(data)

    def addto_file(self,data):
        with open(self.file_name, 'a') as objects:
            objects.write(data)


if __name__ == '__main__':
    file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = os.path.join(file_path1, r'test_files\test_write.txt')
    t = Rw_txt(file_path)
    for i in range(1, 10):
        m = random.randint(10, 100)
        print(str(m)+'\n')
        t.addto_file(str(m)+'\n')



