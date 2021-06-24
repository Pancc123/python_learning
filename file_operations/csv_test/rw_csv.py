# -*- coding:utf-8 -*-
import csv,os


def read_csv(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    reader = csv.reader(f)
    # next()可迭代下一个值
    # words=next(reader) # 首行，一般是标题
    return reader


def write_csv(file_name,data):
    with open(file_name, 'w',encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)  # data必须是如list等可迭代对象


def write_to_csv(file_name,header,value):  # header、value必须是列表或者元组
    with open(file_name, "w",encoding="utf-8", newline="") as fp:  # 其中newline是换行控制的参数，参数有：None，'\n'，'\r'，'\r\n',""(""不换行)
        writer = csv.writer(fp)
        writer.writerow(header)
        writer.writerows(value)


def write_to_csv1(file_name,header,value):  # header可以是列表、元组，value必须是字典
    with open(file_name, "w",encoding="utf-8", newline="") as fp:  # 其中newline是换行控制的参数，参数有：None，'\n'，'\r'，'\r\n'.""
        writer = csv.DictWriter(fp, header)  # 使用csv.DictWriter()方法，需传入两个个参数，第一个为对象，第二个为文件的title
        writer.writeheader()  # 使用此方法，写入表头
        writer.writerows(value)


if __name__ == "__main__":

    '''filename = 'D:/test.csv_test'
    reader = read_csv(filename)
    for row in reader:
        for i in row:
            print(i)'''
    file_path1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    print(file_path1)
    file_path = os.path.join(file_path1, r'test_files\info.csv')
    reader = read_csv(file_path)
    # 方法一
    birth_header = next(reader) # 读取第一行数据，之后reader就只有从第二行开始的数据了
    for user in reader:
        # print(type(user))
        print(user[1])
    # 方法二 将可迭代对象转换成列表
    # data_list = list(reader)
    # for i in data_list:
    #     print(i)
