import xlwt
import xlrd
from xlutils.copy import copy


def write_excel_xls1(i, j, path, sheet_name, value):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name)
    sheet.write(i, j, value)
    workbook.save(path)


# 新建工作簿和表格
def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


def add_sheet(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    rb = xlrd.open_workbook(path)
    wb = copy(rb)
    sheet = wb.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    wb.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


def write_xls2(value,dtuname, path):
    workbook = xlwt.Workbook()
    index = len(value)  # 获取需要写入数据的行数
    sheet = workbook.add_sheet(dtuname)  # 在工作簿中新建一个表格
    first_col = sheet.col(0)
    second_col = sheet.col(1)
    third_col = sheet.col(2)
    first_col.width = 256 * 25
    second_col.width = 256 * 20
    third_col.width = 256 * 25
    style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
    al = xlwt.Alignment()
    al.horz = 0x02  # 设置水平居中
    al.vert = 0x01  # 设置垂直居中
    style.alignment = al
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j], style)  # 像表格中写入数据（对应的行和列）
    print("xls格式表格写入数据成功！")
    workbook.save(path)  # 保存工作簿


def modify_xls(path, sheet_name):
    rb = xlrd.open_workbook(path)
    index1 = rb.sheet_names().index(sheet_name)
    wb = copy(rb)
    # 根据索引查找表格
    ws = wb.get_sheet(index1)
    # 根据表格名称查找表格
    # ws = rb.sheet_by_name()
    first_col = ws.col(0)
    second_col = ws.col(1)
    third_col = ws.col(2)
    first_col.width=256*25
    second_col.width = 256 * 20
    third_col.width = 256 * 15
    wb.save(path)


def read_xls(path):
    #打开xls文档
    data = xlrd.open_workbook(path)
    #获取文档的所有sheet
    sheets=data.sheets()
    #确认读取某一个sheet表，有以下三种方法
    sheet_by_function=sheets[0]
    #sheet_by_index=data.sheet_by_index(0)
    #sheet_by_name= data.sheet_by_name(u'test')
    #查看行列数据
    r1=sheet_by_function.row_values(1)
    c1=sheet_by_function.col_values(1)
    #查看行数和列数
    rows=sheet_by_function.nrows
    cols=sheet_by_function.ncols
    for i in rows:
        print(r1)


if __name__=='__main__':
    book_name_xls = 'D:/xls格式测试工作簿.xls'

    sheet_name_xls = 'xls格式测试表'

    value_title = [["姓名", "性别", "年龄", "城市", "职业"], ]

    write_excel_xls(book_name_xls, sheet_name_xls, value_title)