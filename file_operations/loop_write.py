from js_rw import write_json_file,add_json_file
import random,os


for i in range(1,10):
	t=random.randint(10,100)
	print(t)
	file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
	file_path = os.path.join(file_path1, r'test_files\test_write.json')
	add_json_file(str(t),file_path)
	write_json_file('ok', file_path)
