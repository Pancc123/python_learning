pizza=''
message='\nplease choose a ingredients on pizza:'
message+="\nplease input 'quit' to stop"
while pizza != 'quit':
	pizza=input(message)
	if pizza != 'quit':
	   print(pizza)
	   
message='How old are you ?'
age=''
while True:
	age=input(message)
	if int(age)<3:
		print('you can look the movie for free.')
	elif int(age)<=12:
		print('you need pay 10 dollars for the movie')
	else:
		print('you need pay 15 dollars for the movie')
	if age =='quit':
	   break

     
