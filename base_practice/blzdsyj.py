favorite_languages={'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
friends=['sarah','phil']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(' Hi '+name.title()+',I see your favorite language is '+favorite_languages[name].title()+'!')

word={'best':'the most of goods','big':'samll','beaty':'anger','ji':'ba','ba':'nn'}
for key,value in word.items():
	print(key+': '+value+'\n')
 
river={'nile':'egypt','changjiang':'china','huanghe':'china'}
for key,value in river.items():
	print('The '+key+' runs through '+value)
for key in river.keys():
	print(key)
	
for value in river.values():
	print(value)
