#-*-coding:utf-8-*-
import paho.mqtt.client as mqtt
from com.ioe.metricReport_pb2 import MetricReportRequest
# import com.ioe.metricReport_pb2.MetricReportRequest
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("historyData/analog")
    #data/analog historyData/analog

def on_message(client, userdata, msg):
    target = MetricReportRequest()
    target.ParseFromString(msg.payload)
    for metricData in target.metricData:
        for metric in metricData.metric:
            print("time = "+str(metricData.timestamp)+"; pointid = "+str(metric.pointId)+";value = "+str(metric.value))  
#     print("time = "+str(target.metricData[0].timestamp)+"; pointid = "+str(target.metricData[0].metric[0].pointId)+";value = "+str(target.metricData[0].metric[0].value))
client = mqtt.Client()
client.username_pw_set("yny_mqtt", "yny123")
client.on_connect = on_connect
client.on_message = on_message
client.connect("emq.test3.smarteoc.com", 1883, 60)#i.powercloud.cn
client.loop_forever()
