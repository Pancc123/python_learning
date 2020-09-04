#-*- coding:utf-8 -*-
class Car():
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
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("you can't roll back an odometer !")
	def increment_odometer(self,miles):
		self.odometer_reading+=miles
class ElectricCar(Car):
	"""电动车的独到之处"""
	def __init__(self,make,model,year):
		"""初始化父属性"""
		super().__init__(make,model,year)
		self.battery_size=70
	def describe_battery_size(self):
		print('This car has a '+str(self.battery_size)+'-kwh battery.')

my_tesla=ElectricCar('tesla','model s',2017)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery_size()
