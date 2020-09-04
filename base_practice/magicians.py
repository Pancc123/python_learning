def show_magicians(magicians):
	for mb in magicians:
		name_1='magician: '+mb.title()
		print(name_1)
magicians_name=['liuqian','dazhangwei','panchengcheng']
show_magicians(magicians_name)

def make_great(magicians):
	magicians_1=magicians.pop()
	magicians_2=[]
	while magicians:
	    magicians_2.append('the great '+magicians_1)
make_great(magicians_name)
show_magicians(magicians_2)
		
