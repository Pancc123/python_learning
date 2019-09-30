'''import json
numbers=[2,3,4,5,7,9]
file_name='test.json'
with open (file_name,'w') as f_obj:
	json.dump(numbers,f_obj)'''
	
'''import json

file_name='test.json'
with open(file_name) as f_obj:
	numbers=json.load(f_obj)
	print(numbers)'''


count=0
while(count<9):
	print('The count is:',count)
	count=count+1
	print("Good bye!")
