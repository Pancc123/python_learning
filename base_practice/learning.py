with open('test_files\learning_python.txt') as file_object:
	content=file_object.read()
print(content.rstrip())

		
with open('test_files\learning_python.txt') as file_object:
	for line in file_object:
		print(line.rstrip())
		
		
with open('test_files\learning_python.txt') as file_object:
	mn=file_object.readlines()
for line in mn:
	print(line.rstrip())
