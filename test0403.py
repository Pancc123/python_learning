#!/usr/bin/python3

'''def product(x,y):
	return x*y
	
#测试
#print('product(5)=',product(5))'''
'''try:
	if product(5)!=5:
		print('test fail')
except TypeError:
	print('test fail')'''

'''def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')'''
# -*- coding: utf-8 -*-

'''height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi<18.5:
    print('过轻')
elif bmi<25:
   print('正常')
elif bmi<28:
   print('过重')
elif bim<32:
   print('肥胖')
else:
   print('输入错误')'''
'''io=['string','apple']
for i in io:
	if 'app' in i:
		print('ok')'''
		
'''class Student():
	def __init__(self,name):
		self.name=name
		

	def __str__(self):
		return 'Student object(name:%s)' %self.name

print(Student('Michael'))'''

'''from enum import Enum
Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Agu','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)'''

'''class month(Enum):
	Jan=1
	Feb=2
	Mar=3
	Apr=4
	May=5
	Jun=6
	Jul=7
	Aug=8
	Sep=9
	Oct=10
	Nov=11
	Dec=12
	
month1=month.Jan
print(month1.Jan.value)'''
'''class Gender(Enum):
	male=0
	female=1

class Student():
	def __init__(self,name,age,gender):
		self.name=name
		self.age=age
		self.gender=gender
pcc=Student('pan',15,Gender.male.value)
print(pcc.gender)'''




'''
with open('pcc.txt','r',encoding='utf-8',errors='ignore') as f:
	print(f.read())
with open('pcc.txt','w',encoding='gbk') as f_obj:
	f_obj.write('hello,world!潘')
	for x in os.listdir('.'):
	os.path.getsize(x)
'''
