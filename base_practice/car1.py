# -*- coding:utf-8 -*-
class Car:
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=100
		
	def get_descriptive_name(self):
		"""返回整洁的描述信息"""
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
		
	def read_odometer(self):
		"""打印一条关于汽车里程的消息"""
		print('This car has '+str(self.odometer_reading)+' miles on it.')

	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("you can't roll back an odometer !")

	def increment_odometer(self, miles):
		self.odometer_reading += miles


my_used_car=Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(50)
my_used_car.read_odometer()

my_used_car.increment_odometer(23500)
my_used_car.read_odometer()
