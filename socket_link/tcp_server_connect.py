from socket import *
from time import * 
from threading import *


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' %addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' %data.decode('utf-8')).encode('utf-8'))
        sock.close()
        print('Connection from %s:%s closed.' %addr)


s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1',8888))
s.listen(5)
print('Waitting for connection...')
while True:
    # 接受一个新连接
    sock, addr=s.accept()
    # 创建新线程来处理tcp连接：
    t = Thread(target=tcplink, args=(sock,addr))
    t.start()

