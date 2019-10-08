from file_operations.file_rw import read_txt

t = read_txt("D:\\python_work\\text_files\\user_info.txt")
for line in t.read_file2():
    username = line.split(',')[0]
    password = line.split(',')[1]
    print(username, password)