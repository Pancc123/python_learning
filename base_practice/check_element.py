requested_toppings=['mushroons','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if 'green peppers' == requested_topping:
		print('Sorry,we are out of green peppers.')
	else:
		print('Adding '+requested_topping+'.')
	
requested_toppings=[]
if requested_toppings:
	for request_topping in requested_toppings:
		print('Adding '+requested_topping+'.')
else:
	print('Are you wanting a plain Pizza')
	

user_name=['admin','pan','cheng','wang','zhang','li']
for user_name_1 in user_name:
   if user_name_1=='admin':
	   print('Hello, '+user_name_1)
   else:
	   print('Hello,Eric,thank you for logging again!')

if user_name:
	for user_name_2 in user_name:
		print('we need to find some users!')
	else:
		del user_name
