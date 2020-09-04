cities={
'BeiJing':{'country':'china','population':'100W','fact':'the capital'},
'NewYork':{'country':'American','population':'200W','fact':'Status of libary'},
'Tokyo':{'country':'Japen','population':'110w','fact':'capital'}}
for city_name,city_info in cities.items():
	print('\ncity_name: ',city_name)
	city_all='city_info: '+city_info['country']+'  '+city_info['population']+' '+city_info['fact']
	print('\n'+city_all)

