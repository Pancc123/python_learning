# -*- coding: utf-8 -*-
print('潘')
with open('D:/python_work/gbk.txt','r',encoding='utf-8') as f:
	m=f.read()
print(m)

with open('D:/python_work/my_home.txt','w',encoding='utf-8')as f_obj:
	f_obj.write('潘成成')
	
from io import StringIO
f=StringIO()
m=f.write('hello')
print(m)
n=f.write('')
print(n)
l=f.write('hello world!')
print(l)
print(f.getvalue())
