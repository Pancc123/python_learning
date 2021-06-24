# -*- coding=utf-8 -*
# @Time :  2021-6-3 15:04
# @Author : ChengCheng Pan
import csv


def writer_csv_demo1():
    headers = ["name","age","height"]
    values = [
        ("小王",18,178),
        ("小张",20,180),
        ("小李",17,166)
    ]
    with open(r"D:\\classroom.csv","w",encoding="utf-8",newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)


def read_csv_demo2():
    with open("china_smoking.csv","r") as fp:
        # 使用DictReader创建的reader是一个字典对象，遍历后，不包含第一行数据
        reader = csv.DictReader(fp)
        for x in reader:
            value = {"Location":x["Location"],"smoking_yes_cancer_yes":"smoking_yes_cancer_yes"}
            print(value)


def writer_csv_demo2():
    headers = ["name", "age", "height"]
    values = [
        {"name":"小王","age":18,"height":178},
        {"name":"小王","age":18,"height":178},
        {"name":"小王","age":18,"height":178}
    ]
    with open(r"D:\\classromm2.csv","w", encoding="utf-8",newline="") as fp:
        writer = csv.DictWriter(fp,headers) # 使用csv.DictWriter()方法，需传入两个个参数，第一个为对象，第二个为文件的title
        writer.writeheader()  # 使用此方法，写入表头
        writer.writerows(values)


if __name__ == '__main__':
    writer_csv_demo2()
