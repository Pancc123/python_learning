#! -*- coding:utf-8 -*-
from socket import *
import binascii
from time import sleep
import threading


def equipment_connect(ip,port,msg):
    # 创建一个socket:
    s = socket(AF_INET, SOCK_STREAM)
    # 建立连接
    s.connect((ip, port))
    s.send(msg)  # 发送数据
    while True:
        # d = s.recv(1024)  # 每次最多接受1k字节
        sleep(2)
        s.close()
        sleep(2)


if __name__=='__main__':
    ip = '10.1.170.30'
    port = 6327
    msg = b'0001A5AD01040261'
    msg1 = b'1122334455'
    # t1=equipment_connect(ip, port, msg)
    threads=[]
    t1 = threading.Thread(target=equipment_connect, args=(ip, port, msg,), name='1')
    threads.append(t1)
    t2 = threading.Thread(target=equipment_connect,args=(ip,port,msg1,),name='2')
    threads.append(t2)
    for t in threads:
        t.start()
    for i in threads:
        i.join()

