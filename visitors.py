i=0
while i<=2:
	message=input('please input your name:')
	print('Hello! '+message+'.')
	i+=1
	with open('text_files\guest.txt','a') as file_object:
		file_object.write(message+'\n')
