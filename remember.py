import json
'''filename='username.json'
try:
	with open(filename)as f_obj:
		username=json.load(f_obj)
except FileNotFoundError:
	username=input('What is your name? ')
	with open(filename,'w')as f_obj:
		json.dump(username,f_obj)
		print("We'll remember your name when you come back, "+username+'!')
else:
	print('Welcome back, '+username+'!')'''
def get_stored_name():
	file_name='username.json'
	try:
		with open(file_name) as f_obj:
			username=json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
def get_new_name():
	username=input('What is your name? :')
	file_name='username.json'
	with open(file_name,'w') as f_obj:
		json.dump(username,f_obj)
	return username
def greet_user():
	username=get_stored_name()
	user_name=input('please input your name:')
	if username==user_name:
		print('Welcome back, '+username+'.')
	else:
		username=get_new_name()
		print("We'll remember your name when you come back, "+ username+'.')
		
greet_user()
		
		
