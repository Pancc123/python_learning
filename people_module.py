# -*- coding: utf-8 -*-


class people:
    age = 0
    __weight = 0

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s%d" %(self.name,self.age))


class people1:
    name = ''
    age = 0
    __weight = 0

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s%d" %(self.name,self.age))


if __name__ == "__main__":
    p = people1('runoob', 10, 30)
    p.speak()
    m = people('runoob', 10, 30)
    m.speak()
