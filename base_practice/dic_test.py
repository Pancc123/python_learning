alien_0={'color':'green','point':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=23
print(alien_0)
print('\n')
del alien_0['color']
print(alien_0)


zhangshan={'frist_name':'zhang','second':'shan','age':34,'city':'hangzhou'}
print(zhangshan)

favorite_digital={'liwei':3,'zhuhong':5,'zhaowei':6,'panchengcheng':8}
print(favorite_digital)


favorite_languages={'jen':'python','sarah':'c','edward':'rudy','phil':'phthon'}
for name,language in favorite_languages.items():
	print(name.title()+"'s favorite language is "+language.title())
for name in favorite_languages.keys():
	print(name.title())
