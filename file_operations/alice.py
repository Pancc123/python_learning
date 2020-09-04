filename='test_files\\alice.txt'

try:
	with open(filename) as fb_obj:
		contents=fb_obj.read()
except FileNotFoundError:
	msg='Sorry,the file '+filename+" does not exist."
	print(msg)
else:
	words=contents.split()
	num_words=len(words)
	print('The file '+filename+' has about '+str(num_words)+' words.')
