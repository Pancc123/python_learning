print('please input 2 digital:')
while True:
	a=input('the first: ')
	if a=='q':
		break
	b=input('the second: ')
	try:
		print(int(a)+int(b))
	except ValueError:
		print('the inputs are not digital,please input again.')
