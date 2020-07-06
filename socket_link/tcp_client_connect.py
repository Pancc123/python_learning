# 导入socket 库
from socket import *
import binascii


# 输出tcp-server 返回的内容
def tcp_client(ip, port,msg):
    # 创建一个socket:
    s = socket(AF_INET, SOCK_STREAM)
    # 建立连接
    s.connect((ip, port))  # s.connect(('www.sina.com.cn',80))
    s.send(msg)  # 发送数据
    # s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    # b'' 转换为bytes类型
    buffer = []
    while True:
        d = s.recv(1024)  # 每次最多接受1k字节
        if not d:
            break
        else:
            d = binascii.b2a_hex(d)
            print(d.decode("utf-8"))
            buffer.append(d)
    data1 = b''.join(buffer)
    # print(data1)
    s.close()
    return data1


# 阻塞式
def tcp_client1(ip, port, msg):
    # 创建一个socket:
    s = socket(AF_INET, SOCK_STREAM)
    # 建立连接
    s.connect((ip, port))  # s.connect(('www.sina.com.cn',80))
    s.send(msg)  # 发送数据
    while True:
        try:
            d = s.recv(1024)  # 每次最多接受1k字节
            if not d:
                break
            else:
                send_frame = msg  # 填写发送数据
                s.send(bytes().fromhex(send_frame))
                # s.send(send_frame.encode('utf-8'))
                # print(data)
        except Exception as e:
            print(e)
            break
    # data1 = b''.join(buffer)
    print("disconnected")
    s.close()


def output_msg(data):
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接受的数据写入文件：
    with open('tcp.html', 'wb') as f:
        f.write(html)


if __name__ == '__main__':
   ip='10.1.170.30'
   port=6327
   msg=b'0001A5AD01040261'
   data=tcp_client(ip,port,msg)
