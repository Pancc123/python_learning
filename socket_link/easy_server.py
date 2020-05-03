from socket import *
from time import ctime
import time

host = ''
port = 12345
buffsize=2048
addr=(host,port)

tctime = socket(AF_INET,SOCK_STREAM)
tctime.bind(addr)
tctime.listen(5)

while True:
	print('Wait for connection ...')
	tctimeClient, addr = tctime.accept()
	print('Connection from:', addr)

	while True:
		data = tctimeClient.recv(buffsize).decode('utf-8')
		time.sleep(2)
		if not data:
			break
		print(data)
		tctimeClient.send(('[%s]%s' % (ctime(), data)).encode('utf-8'))
	tctimeClient.close()

tctimeClient.close()

