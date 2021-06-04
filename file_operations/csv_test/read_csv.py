# -*- coding:utf-8 -*-
import csv,os


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


def read_csv_demo2():
    with open("china_smoking.csv","r") as fp:
        # 使用DictReader创建的reader是一个字典对象，遍历后，不包含第一行数据
        reader = csv.DictReader(fp)
        for x in reader:
            value = {"Location":x["Location"],"smoking_yes_cancer_yes":"smoking_yes_cancer_yes"}
            print(value)


if __name__ == "__main__":

    '''filename = 'D:/test.csv_test'
    reader = read_csv(filename)
    for row in reader:
        for i in row:
            print(i)'''
    file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = os.path.join(file_path1, r'test_files\info.csv_test')
    reader = read_csv(file_path)
    birth_header = next(reader) # 读取第一行数据，之后reader就只有从第二行开始的数据了
    for user in reader:
        # print(type(user))
        print(user[1])
