pet_0={'type':'cat','master':'pan'}
pet_1={'type':'dog','master':'li'}
pet_2={'type':'pig','master':'wang'}
pet=[pet_0,pet_1,pet_2]
for pet_name in pet:
	for key,value in pet_name.items():
		print(key+"'s:"+value+'\n')


message=input('please enter your name:')
print('Hello,'+message)

prote='\n Tell me something,I will repeat for you:'
prote+="\ntry again,enter 'quit' to end the program!"
active=True
while active:
	message=input(prote)
	if message =='quit':
	   active=False
	else:
	   print(message)
