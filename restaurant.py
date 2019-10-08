#-*- coding:utf-8 -*-
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	def describe_restaurant(self):
		print('The name of restaurant is '+self.restaurant_name.title())
		print('The cuisine_type of restaurant is '+self.cuisine_type+'.')
	def open_restaurant(self):
		print(self.restaurant_name.title()+' is opening!')
		
		
restaurant=Restaurant('saibwei','川菜')
restaurant.open_restaurant()
restaurant.describe_restaurant()
