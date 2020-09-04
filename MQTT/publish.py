#-*-coding:utf-8-*-
import paho.mqtt.client as mqtt
import time


HOST = 'mqtt2.smarteoc.com'
PORT = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    #client.subscribe("topic/test")
    client.subscribe("device/0001/gw/protobuf-v1/config/0/0005100C01022400", qos=0)


def on_message(client, userdata, msg):
    print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))


def client_loop():
    client = mqtt.Client()
    client.username_pw_set("pcc@host1", "yny123")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()


if __name__ == '__main__':
    client_loop()
'''for i in range(1, 100):
	print ("send msg = test"+str(i))
	client.publish("test","test"+str(i))'''
