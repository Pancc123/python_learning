def show_magicians(magicians_name):
	for name in magicians_name:
		print('magicians: '+ name.title())
def make_great(magicians_name,new_name):
	while magicians_name:
		msg=magicians_name.pop()
		new='the great ' +msg
		new_name.append(new)

magicians_name=['liuqian','cheng','chao']
new_name=[]
make_great(magicians_name,new_name)
show_magicians(new_name)
