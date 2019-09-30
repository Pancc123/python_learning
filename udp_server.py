from socket import *
from time import *
s=socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
#绑定端口
print('waitting for connection....')
while True:
	
	#接受数据
	data,addr=s.recvfrom(1024)
	print('Received from %s:%s' %addr)
	if not data: 
		break
	#print(data.decode('utf-8'))
	#s.sendto(b'%s,Hello,%s!' %(ctime(),data).decode('utf-8'),addr)
	s.sendto((('[%s]%s' %(ctime(),data)).encode('utf-8')),addr)
'''
s = socket(AF_INET, SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)'''
