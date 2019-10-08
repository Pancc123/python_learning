def countword(file_names):
	try:
		with open(file_names) as fb_obj:
			contents=fb_obj.read()
	except FileNotFoundError:
		#msg='Sorry,the file '+file_names+" does not exist."
		#print(msg)
		pass
	else:
		words=contents.split()
		num_words=len(words)
		print('The file '+file_names+' has about '+str(num_words)+' words.')
file_name=['text_files\\alice.txt','text_files\\alice1.txt','text_file\\alice3.txt','text_files\\alice2.txt']
for file_names in file_name:
	countword(file_names)
	

