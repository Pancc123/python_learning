#-*- coding:utf-8 -*-
class User():
	def __init__(self,first_name,last_name,age,location):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.location=location
	def describe_user(self):
		print('His name is '+self.first_name.title()+self.last_name.title()+'.')
		print("He is "+str(self.age)+' years old.')
		print("He is from "+self.location.title()+'.')
	def greet_user(self):
		print('Hello,'+self.first_name.title()+self.last_name.title()+'.')


zhang=User('zhang','san',23,'zhejiang')
zhang.describe_user()
zhang.greet_user()
