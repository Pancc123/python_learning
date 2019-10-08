file_name='text_files//learning_python.txt'
with open(file_name) as file_object:
	line=file_object.readlines()
for mn in line:
	mn=mn.replace('Python','C')
	print(mn.rstrip())
