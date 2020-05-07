from file_operations.txt_read import read_txt

file_name = 'D:\\python_work\\test_files\\pi_digits.txt'
t = read_txt(file_name)
data = t.read_file()
print(data.rstrip())


with open(file_name, 'r') as file_object:
    for line in file_object:
        print(line.rstrip())


lines = t.read_file2()
for line in lines:
    print(line.rstrip())


pi_string = ''
for line in lines:
    pi_string += line.strip()
    print(pi_string)
    print(len(pi_string))
