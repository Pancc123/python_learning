import os
import shutil
# shutil可以实现文件的复制，移动


def print_animal(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = 'Sorry,the file ' + filename + ' not exist.'
		print(msg)
		shutil.move('except\\cat.txt','test_files\\cat.txt')
	else:
		print(contents)


filenames = ['test_files\\cat.txt', ]
for filename in filenames:
	print_animal(filename)
