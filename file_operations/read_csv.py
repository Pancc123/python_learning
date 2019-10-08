# -*- coding:utf-8 -*-
import csv


def read_csv(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    reader = csv.reader(f)
    # next()可迭代下一个值
    # words=next(reader)
    return reader


def write_csv(file_name,data):
    with open(file_name, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)  # data必须是如list等可迭代对象


if __name__ == "__main__":

    '''filename = 'D:/test.csv'
    reader = read_csv(filename)
    for row in reader:
        for i in row:
            print(i)'''
    filename = "D:\\python_work\\text_files\\info.csv"
    reader = read_csv(filename)
    for user in reader:
        # print(user)
        print(user[1])
