# -*- coding:utf-8 -*-
import re
file_name='imu.txt'

L_station = []
happen_point= []
L_happen = []
dict1={}
with open(file_name,'r',encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        station_list=re.findall(r'80\w{14}"',line)
        station_code=''.join(station_list)
        L_station.append(station_code)
    for line1 in data:
        happen_list=re.findall(r'"happenTime":\d{10}', line1)
        station_list1 = re.findall(r'80\w{14}"', line1)
        happen_time=happen_list[0]
        happen_Time=re.findall(r'\d{10}', happen_time)
        happen_TTime=happen_Time[0]
        happen_int = int(happen_TTime)
        if happen_int in range(1531903200, 1531905300):
            happen_point.append(station_list1[0])

station_counts=list(set(L_station))
print(len(station_counts))
#总站数
happen_points=list(set(happen_point))
print(len(happen_points))
#事故时间出现告警站数













'''(t=re.findall(r'"happenTime":\d{10}', line)

 gg=re.findall(r'80\w{14}"', line)
 ii=gg[0]
 souts.append(ii)



n = ''.join(t)
p = re.findall(r'\d{10}', n)
o = ''.join(p)
tt = int(o)
#print(tt)
if tt not in range(1531903200, 1531905300):
 N=[]
L.append(tt)
pp = re.findall(r'80\w{14}"', line)
 kk= ''.join(pp)
N.append(kk)


print(lent(sort))
print(len(L))
print(len(N))
'''

#mm=list(set(N))
#print(len)




#print(len(L))'''

          # ''' m =''.join(m)
           # if m not in range(1531903200, 1531905300):
              # L.append(m)
               #print(L)'''