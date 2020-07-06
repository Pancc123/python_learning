import json
'''fav_digtal=input('Please input you favourite digtal: ')
file_name='digtal.json'
with open(file_name,'w') as f_obj:
	json.dump(fav_digtal,f_obj)
with open(file_name) as f_obj:
	fav_digtal=json.load(f_obj)
	print("I know your favorite number! It's "+fav_digtal+'.')'''


def words():
	file_name='digtal.json'
	try:
		
		with open(file_name) as f_obj:
			fav_digtal=json.load(f_obj)
	except FileNotFoundError:
		fav_digtal=input('Please input you favourite digtal: ')
		
		with open(file_name,'w') as f_obj:
			json.dump(fav_digtal,f_obj)
	else:
		print("I know your favorite number! It's "+fav_digtal+'.')


words()
