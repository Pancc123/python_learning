#-*- coding:utf-8 -*-
class User():
	def __init__(self,first_name,last_name,age,location):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.location=location
		self.login_attempts=0
	def describe_user(self):
		print('His name is '+self.first_name.title()+self.last_name.title()+'.')
		print("He is "+str(self.age)+' years old.')
		print("He is from "+self.location.title()+'.')
	def greet_user(self):
		print('Hello,'+self.first_name.title()+self.last_name.title()+'.')
	def increment_login_attempts(self):
		self.login_attempts+=1
	def reset_login_attempts(self):
		self.login_attempts=0


wang=User('wanp','peng',18,'zhejiang')
wang.increment_login_attempts()
wang.increment_login_attempts()
#print(wang.login_attempts)
wang.reset_login_attempts()
print(wang.login_attempts)
