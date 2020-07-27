from socket import *
from time import ctime
import time
from threading import *

host = ''
port = 12345
buffsize=2048
addr=(host,port)
conn_list=[]


def tcplink(sock, addr):
	sock.send(b'Welcome!')
	while True:
		try:
			data = sock.recv(1024)
			time.sleep(1)
			if not data or data.decode('utf-8') == 'exit':
				break
			sock.send(('Hello,%s!' %data.decode('utf-8')).encode('utf-8'))
		except Exception as e:
			print(e)
			break
	sock.close()
	print('Connection from %s:%s closed.' %addr)


if __name__=='__main__':
	tctime = socket(AF_INET, SOCK_STREAM)
	tctime.bind(addr)
	tctime.listen(5)
	while True:
		# 接受一个新连接
		sock, addr = tctime.accept()
		print('Accept new connection from %s:%s...' % addr)
		conn_list.append(sock)
		# 创建新线程来处理tcp连接：
		t = Thread(target=tcplink, args=(sock, addr))
		t.start()
		t.join()

