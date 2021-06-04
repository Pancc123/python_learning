from json_test.js_rw import write_to_jsf,add_to_jsf
import random,os


for i in range(1,10):
	t=random.randint(10,100)
	print(t)
	file_path1 = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
	file_path = os.path.join(file_path1, r'test_files\test_write.json_test')
	add_to_jsf(str(t),file_path)
	write_to_jsf('ok', file_path)
