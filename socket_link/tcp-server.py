# -*-coding:utf-8 -*-
import binascii
import datetime
import re
import socket
import traceback
from time import sleep
from influxdb import InfluxDBClient
import socketserver

conn_poll = []


class MyServer(socketserver .BaseRequestHandler):

    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        # print(self.client_address)
        conn.settimeout(120)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Accept new connection from {}:...:".format(self.client_address))
        conn_poll.append(self.client_address)
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.client_address, '的链接断开了！')  # 等待接收但接收为空则客户端断开
                    # self.remove()
                    conn_poll.remove(self.client_address)
                    break
                hexstr = str(binascii.b2a_hex(data))[2:-1]
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "收到客户端数据（十六进制）recv：" + hexstr)
                sleep(1)
                # for c in self.client_address:
                #     c.send(('Hello,%s!' %data.decode('utf-8')).encode('utf-8'))
                conn.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "发送数据（十六进制）send：" + hexstr)
            except ConnectionResetError:              # 捕捉客户端关闭信息
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '{} connection closed'.format(self.client_address))
                conn_poll.remove(self.client_address)
                break
            finally:
                pass
        conn.close()


if __name__ == '__main__':
    server = socketserver .ThreadingTCPServer(('192.168.10.175', 8844), MyServer)
    print("server 启动")
    server.serve_forever()
