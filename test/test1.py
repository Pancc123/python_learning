# -*- coding=utf-8 -*
# @Time :  2021-1-27 20:05
# @Author : ChengCheng Pan

from io import StringIO

import csv

import pandas as pd

c_path = r'D:\N3-K网管-Kddi新增功能-用例.csv'

x_path = r'D:\N3-K网管-Kddi新增功能-用例1.xlsx' # 路径中的xls文件在调用to_excel时会自动创建


def csv_to_xls(c_path, x_path):
    with open(c_path, 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)
        data_file = StringIO(data)
        print(data_file)
        csv_reader = csv.reader(data_file)
        print(csv_reader)
        list_csv = []

        for row in csv_reader:
            list_csv.append(row)
            df_csv = pd.DataFrame(list_csv).applymap(str)
            print(df_csv)

    writer = pd.ExcelWriter(x_path)
    # 写入Excel
    df_csv.to_excel(excel_writer=writer,index=False,header=False )
    writer.save()