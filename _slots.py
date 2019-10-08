from types import MethodType

'''class Student():
	pass
s=Student()
def set_age(self,age):
	self.age=age
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)'''
'''class Car():
	pass
	def car_name(self,name):
	   self.name=name
	   
ltt=Car()
ltt.car_name('cc')
print(ltt.name)'''
'''lass Student():
	__slots__=('name','age')
s=Student()
s.name='pcc'
s.age=25
s.height=171'''
'''from datetime import datetime

print(datetime.now())
now=datetime.now()
print(type(now))
print(now.timestamp())

print(datetime.utcfromtimestamp(now.timestamp()))
print(datetime.strptime('2017-9-12 18:21:23','%Y-%m-%d %H:%M:%S'))'''

''' collections import namedtuple,deque
Point=namedtuple('Point',['x','y'])
d=Point(1,2)
print(d.x)

q=deque(['a','b','c'])
q.append('d')
q.appendleft('x')
print(q)'''

