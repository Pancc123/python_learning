#-*- coding:utf-8 -*-
class myclass():
	height=171
	def f(self):
		return 'hello world !'
#实例化类
x=myclass()
print('His height is : ',x.height)
print('the word he said for the first time is:',x.f())




#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说他的年龄是%d" %(self.name,self.age))
 
class simple(people):
	grade=''
	def __init__(self,n,a,w,g):
		people.__init__(self,n,a,w)
		self.grade=g
	def speak(self):
		print('%s他说他的年龄是%' %(self.name,self.age))
		
y=people('pcc',12,65)
y.speak()

