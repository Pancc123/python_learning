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
		
		
class Battery():
	def __init__(self,battery_size=60):
		self.battery_size=battery_size
	def describe_battery(self):
		print('This car has a '+str(self.battery_size)+'-kwh battery.')
	def get_range(self):
		if self.battery_size==85:
			range=270
		else:
			range=240
			self.battery_size=85
		message='This car can go approximately ' +str(range)
		message+=' miles on a full charge.'
		print(message)
		
class ElectricCar(Car):
	"""电动车的独到之处"""
	def __init__(self,make,model,year):
		"""初始化父属性"""
		super().__init__(make,model,year)
		self.battery=Battery()
		
my_tesla=ElectricCar('tesla','model s',2017)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.get_range()

