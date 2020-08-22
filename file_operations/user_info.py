from txt_rw import Rw_txt
import os

file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_path = os.path.join(file_path1, r'test_files\user_info.txt')

t = Rw_txt(file_path)
for line in t.read_file2():
    username = line.split(',')[0]
    password = line.split(',')[1]
    print(username, password)
