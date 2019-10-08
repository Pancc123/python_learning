favorite_place={'zhuhong':['beijing','shanghai'],'sunke':['shanhai','hangzhou'],'liutao':['hongkong','guangzhou','chengdu']}
for name,place in favorite_place.items():
	print(name+"'s favorite_place:")
	for value in place:
	    print(value.title())
	print('\n')
   
