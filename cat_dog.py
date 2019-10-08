import os
import shutil
def print_animal(filename):
	try:
		with open(filename) as f_obj:
			contents=f_obj.read()
	except FileNotFoundError:
		msg='Sorry,the file '+ filename +' not exist.'
		print(msg)
		shutil.move('text_files\cat.txt','except\cat.txt')
	else:
		print(contents)

filenames=['text_files\cat.txt','text_files\dog.txt']
for filename in filenames:
	print_animal(filename)
