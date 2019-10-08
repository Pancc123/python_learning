#-*- coding:utf-8 -*-
class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.oldmeter_reading=0
		
	def get_descriptive_name(self):
		"""返回整洁的描述信息"""
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
		
	def read_odometer(self):
		"""打印一条关于汽车里程的消息"""
		print('This car has '+str(self.oldmeter_reading)+' miles on it.')


my_new_car=Car('aoui','A4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

