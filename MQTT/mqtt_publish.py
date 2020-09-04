# -*-coding:utf-8-*-
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


client = mqtt.Client()
client.username_pw_set("yny_mqtt", "yny123")
client.on_connect = on_connect
client.connect("i.powercloud.cn", 1883, 60)
for i in range(1, 100):
    print ("send msg = test"+str(i))
    client.publish("test","test"+str(i))
