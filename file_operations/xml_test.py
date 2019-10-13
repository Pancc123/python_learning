#! -*- coding:utf-8 -*-
from xml.etree.ElementTree import parse, Element

with open("C:/Users/dell/Desktop/MODBUS-RTU_7846_SMA SOLID-Q 50.xml", "rt", encoding='utf-8') as f:
    tree = parse(f)
    root = tree.getroot()
    data = root.getchildren()
    for child in data[0][1]:
        print(child.attrib)
        test=child.attrib
        dd=test['key']
        print(dd)
        ds=test['funcode']
        dds=int(ds)+1
        ds='0'+str(dds)
        print(ds)


