def make_great(magicians_name,new_name):
	while magicians_name:
		msg=magicians_name.pop()
		new='the great' +msg
		new_name.append(new)
