from socket import *
host='localhost'
port=12345
buffersize=2048
addr=(host,port)
tctimeClient=socket(AF_INET,SOCK_STREAM)
tctimeClient.connect(addr)
while True:
	data = input('>')
	if not data :
		break
	tctimeClient.send(data.encode('utf-8'))
	data=tctimeClient.recv(buffersize).decode('utf-8')
	if not data or data=='exit':
		break
	print(data)
tctimeClient.close()
		
