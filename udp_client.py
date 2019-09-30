from socket import *

'''s=socket(AF_INET,SOCK_DGRAM)

for data in [b'Michael',b'Tracy',b'Sarah']:
	#发送数据
	s.sendto(data,('127.0.0.1',9999))
	#接受数据
	data=s.recv(1024).decode('utf-8')
	if not data or data=='exit':
		break
	print(data)
s.close()'''
s = socket(AF_INET, SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    data=s.recv(1024)
    print(data.decode('utf-8'))
s.close()
