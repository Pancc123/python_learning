uncomfirmed_users=['alice','brian','candace']
comfirmed_users=[]
while uncomfirmed_users:
	current_user = uncomfirmed_users.pop()
	comfirmed_users.append(current_user)
	print('Verifying user:' + current_user.title())
    #comfirmed_users.append(current_user)
    #comfirmed_users.append()
   
print('\n The following users have been comfirmed:')
for user in comfirmed_users:
	print(user.title())


sandwich_orders=['apple','banana','apple','orange','apple']
finished_sandwiches=[]
while sandwich_orders:
	current=sandwich_orders.pop()
	print('I made your tuna sandwich: '+ current)
	finished_sandwiches.append(current)
for sandwich in finished_sandwiches:
	print("all the sandwich:" +sandwich)
print('apple was selled out')
while 'apple'in finished_sandwiches:
	finished_sandwiches.remove('apple')
print(finished_sandwiches)

response={}
message1='\n what is your name?'
message='\nIf you could visit one place in the world,where would you go?'
while True:
	message2=input(message1)
	response[message2]=input(message)
	repeat=input('would you want to stop?yes/no')
	if repeat =='no':
	   break
for message2,message in response.items():
    print(message2+ 'would like vist '+message)
