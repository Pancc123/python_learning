# -*- coding=utf-8 -*
# @Time :  2021-1-22 15:07
# @Author : ChengCheng Pan
import pandas as pd
import xlwt,csv
from io import StringIO


def csv_to_xlsx_pd(old_file,new_file,sheet_name):
    csv = pd.read_csv(old_file, encoding='utf-8')
    print(csv)
    csv.to_excel(new_file, sheet_name=sheet_name)


# csv转xlsx
def csv_to_xlsx(c_path, x_path,sheet_name):
    with open(c_path, 'r', encoding='utf-8') as f:
        data = f.read()
        # print(data)
        data_file = StringIO(data)
        # print(data_file)
        csv_reader = csv.reader(data_file)
        # print(csv_reader)
        list_csv = []

        for row in csv_reader:
            list_csv.append(row)
            df_csv = pd.DataFrame(list_csv).applymap(str)
            # print(df_csv)

    writer = pd.ExcelWriter(x_path)
    # 写入Excel
    df_csv.to_excel(excel_writer=writer,index=False,header=False,sheet_name=sheet_name )
    writer.save()


def csv_to_xlsx1(csvfile,outfile,sheet_name):
    with open(csvfile, encoding='utf-8') as fc:
        r_csv = csv.reader(fc)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet(sheet_name)  # 创建一个sheet表格
        i = 0
        j = 0
        for line in r_csv:
            for v in line:
                sheet.write(i,j,v)
                j = j + 1
            i = i + 1
        workbook.save(outfile)  # 保存Excel





if __name__ == '__main__':

    pass