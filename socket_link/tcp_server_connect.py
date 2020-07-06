from socket import *
from time import * 
from threading import *


def tcp_hande(sock, addr):
    print('Accept new connection from %s:%s...' %addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        print(data)
        sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' %data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' %addr)


# 多线程
def tcp_hande1(sock_list,i):
    sock = i[0]
    addr = i[1]
    sock.send(b'Welcome!')
    while True:
        try:
            data = sock.recv(1024)
            print(data)
            sleep(1)
        except Exception as e:
            sock_list.remove(i)
            break
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' %data.decode('utf-8')).encode('utf-8'))
    print('Connection from %s:%s closed.' % addr)
    sock.close()


def test(sock_list):
    for i in sock_list:
        t = Thread(target=tcp_hande1, args=(sock_list,i ))  # sock=i[0],addr=i[1]
        t.join()


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('192.168.1.9',8888))
    s.listen(5)
    print('Waitting for connection...')
    while True:
        # 接受一个新连接
        sock, addr = s.accept()
        # sock.setblocking(0) 设置非阻塞
        # 创建新线程来处理tcp连接：
        t = Thread(target=tcp_hande, args=(sock,addr))
        t.start()
        # t.join() 使用join()后，只有子线程结束后才能执行接下来的主线程。

