#! -*- :utf-8 -*-
'''d={'x':'A','y':'B','z':'C'}
L=[key+'='+value for key,value in d.items()]
print(L)
'''
'''from functools import reduce

def add(x,y):
	return x+y
t=reduce(add,[1,2,3,4])
print(t)'''
'''def triangel(n):
    L=[1]                                                               
    while True:
        yield L                                                         
        L=[L[x]+L[x+1] for x in range(len(L)-1)]        
        L.insert(0,1)                                                
        L.append(1)                                                 
        if len(L)>10:                                                 
            break
            
a=triangel(10)
for i in a:
    print(i)'''
'''def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

def _not_divsiable(n):
	return lambda x: x%n>0
	
def primes():
	yield 2
	it=_odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(_not_divsiable(n),it)

for n in primes():
	if n<1000:
		print(n)
	else:
		break'''


class Student:
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count += 1


new_school=Student('pan')
print(new_school.count)
