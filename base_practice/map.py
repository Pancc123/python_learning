def normalize(name):
	for name1 in name:
	   a=name.lower()
	   b=a.title()
	   return b
L1=['admin','LIAS','taBLE']
L2=list(map(normalize,L1))
print(L2)

'''from functools import reduce as kj
def pro(x,y):
	return x*y
L1=[1,2,2,7]
L2=kj(pro,L1)
print(L2)'''
	
