import xlrd
import xlwt
from xlutils.copy import copy


def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


book_name_xls = 'D:/xls格式测试工作簿.xls'

sheet_name_xls = 'xls格式测试表'

value_title = [["姓名", "性别", "年龄", "城市", "职业"], ]

write_excel_xls(book_name_xls, sheet_name_xls, value_title)
