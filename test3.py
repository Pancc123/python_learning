#-*- coding: utf-8 -*-
class people:
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s%d" %(self.name,self.age))
m = people('runoob',10,30)
m.speak()

class people:
    #�����������
    name = ''
    age = 0
    #����˽������,˽�����������ⲿ�޷�ֱ�ӽ��з���
    __weight = 0
    #���幹�췽��
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s%d" %(self.name,self.age))
 
# ʵ������
p = people('runoob',10,30)
p.speak()
