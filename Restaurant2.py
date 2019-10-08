#-*- coding:utf-8 -*-
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0
	def set_number_served(self,number_served):
		self.number_served=number_served
	def increment_number_served(self,increment_number):
		self.number_served+=increment_number
		
		
restaurant=Restaurant('KFC','Fast food')
restaurant.set_number_served(100)
print('There are '+str(restaurant.number_served)+' number of customers having a meal in '+restaurant.restaurant_name+'.')
#print('There are  '+ str(restaurant.number_served)+ ' having a meal in '+restaurant.restaurant_name())
restaurant.increment_number_served(50)
print('Do you konw how many customers will increase everyday?'+'\n'+str(restaurant.number_served))
