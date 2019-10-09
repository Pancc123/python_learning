i=1
while i<=3:
	message=input('why dou like programing?')
	i+=1
	with open('text_files\programmig.txt','a')as file_object:
		file_object.write(message+'\n')

