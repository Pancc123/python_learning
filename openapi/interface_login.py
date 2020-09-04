#! -*- coding:utf-8 -*-
import requests
data = {'username': 'admin_yny', 'password': 'yny123'}
url = 'http://www.smarteoc.com/api/latest/user/serviceProviderLogin'
headers = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','Authorization':\
'Bearer null','Connection': 'keep-alive','Content-Type':'application/json','Content-Type':\
'zg_did=%7B%22did%22%3A%20%221622d54d858a86-084d43d3c38b27-5f4f2816-1fa400-1622d54d8592f6%22%7D; userLogo=null; \
currentCustomerId=CompanyService:1498120229607; curStationId=assetaccount/t_powerclient:1508825745995;\
 dlqsDeviceId=assetaccount/t_powerclient:1508825745995; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\
 eyJpYXQiOiIxNTM0MjQ0Mzk3MDA4IiwiZXhwIjoxNTM0MjQ0NDAwNjA4LCJ0b2tlbkluZm8iOnsiZXhwUGFyYW0iOiIxIn0sImVtcGxveWVlSWQiO\
 iJFbXBsb3llZVNlcnZpY2U6MTQ5ODEyMDI1NzA1MSIsInBvc2l0aW9uIjoi57O757uf566h55CG5bKXIiwiaWNvbiI6Imh0dHA6Ly9pbWcub3NzLnBvd\
 2VyY2xvdWQuY24vM0E3RjkzQjQtQjQ1Qi00OUY3LUJEMkMtM0JBMzVCOUZFOUE4MTUxMjExNDIwNDEwNiIsInNleCI6IueUtyIsImFjY291bnRJZCI\
 6ImFjY291bnQvYWNjb3VudDoxNDk4MTIwMjc5NjcyIiwiY29tcGFueU5hbWUiOiLlubPlj7DmtYvor5UiLCJkZXBhcnRtZW50TmFtZSI6IiIsImVt\
 cGxveWVlTmFtZSI6Iua1i-ivlSIsImNvbXBhbnlDb2RlIjoiMTAxMDg5Yzk1YTc4ZDZkNCIsImN1c3RvbWVySWQiOiJDb21wYW55U2VydmljZ\
 ToxNDk4MTIwMjI5NjA3IiwiY2VsbHBob25lIjoiMTQxMTIzNDU2NzgiLCJzaG9ydE5hbWUiOiLlubPlj7DmtYvor5UiLCJ1c2VyIjoicHR0ZXN0Iiwi\
 Y29tcGFueUNoYXJhY3RlciI6WyIwMiIsIjA0IiwiMTAiLCIwOSJdLCJpc1N0YXRpb24iOmZhbHNlLCJzZXJ2aWNlUHJvdmlkb3JOYW1lIjoi5bmz5Y-w5\
 rWL6K-VIiwic2VydmljZVByb3ZpZG9ySWQiOiJDb21wYW55U2VydmljZToxNDk4MTIwMjI5NjA3Iiwic2VydmljZVByb3ZpZG9yU2hvcnROYW1lIjoi5\
 bmz5Y-w5rWL6K-VIn0.gRul1yTzkWqwh3IJ_5NsrhUtZI-6dFZKPosaiDvggpg; token.sig=EIWhgP_d96xVGyR-ph16nfTCpHg; user={"em\
 ployeeId":"EmployeeService:1498120257051","position":"ç³»ç»ç®¡çå²","icon":"http://img.oss.powercloud.cn/3A7F\
 93B4-B45B-49F7-BD2C-3BA35B9FE9A81512114204106","sex":"ç·","accountId":"account/account:1498120279672","companyNa\
 me":"å¹³å°æµè¯","departmentName":"","employeeName":"æµè¯","companyCode":"101089c95a78d6d4",\
 "customerId":"CompanyService:1498120229607","cellphone":"14112345678","shortName":"å¹³å°æµè¯","user":"pttest",\
 "companyCharacter":["02","04","10","09"],"isStation":false,"serviceProvidorName":"å¹³å°æµè¯","service\
 ProvidorId":"CompanyService:1498120229607","serviceProvidorShortName":"å¹³å°æµè¯","iat":"1534244397008",\
 "logo":null,"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNTM0MjQ0Mzk3MDA4IiwiZXhwIjoxNTM0MjQ0NDAwNjA4L\
 CJ0b2tlbkluZm8iOnsiZXhwUGFyYW0iOiIxIn0sImVtcGxveWVlSWQiOiJFbXBsb3llZVNlcnZpY2U6MTQ5ODEyMDI1NzA1MSIsInBvc2l0aW9uIjoi5\
 7O757uf566h55CG5bKXIiwiaWNvbiI6Imh0dHA6Ly9pbWcub3NzLnBvd2VyY2xvdWQuY24vM0E3RjkzQjQtQjQ1Qi00OUY3LUJEMkMtM0JBMzVCOUZFO\
 UE4MTUxMjExNDIwNDEwNiIsInNleCI6IueUtyIsImFjY291bnRJZCI6ImFjY291bnQvYWNjb3VudDoxNDk4MTIwMjc5NjcyIiwiY29tcGFueU5hb\
 WUiOiLlubPlj7DmtYvor5UiLCJkZXBhcnRtZW50TmFtZSI6IiIsImVtcGxveWVlTmFtZSI6Iua1i-ivlSIsImNvbXBhbnlDb2RlIjoiMTAxMDg5Yzk1Y\
 Tc4ZDZkNCIsImN1c3RvbWVySWQiOiJDb21wYW55U2VydmljZToxNDk4MTIwMjI5NjA3IiwiY2VsbHBob25lIjoiMTQxMTIzNDU2NzgiLCJzaG9ydE5hb\
 WUiOiLlubPlj7DmtYvor5UiLCJ1c2VyIjoicHR0ZXN0IiwiY29tcGFueUNoYXJhY3RlciI6WyIwMiIsIjA0IiwiMTAiLCIwOSJdLCJpc1N0YXRpb24iO\
 mZhbHNlLCJzZXJ2aWNlUHJvdmlkb3JOYW1lIjoi5bmz5Y-w5rWL6K-VIiwic2VydmljZVByb3ZpZG9ySWQiOiJDb21wYW55U2VydmljZToxNDk4MTI\
 wMjI5NjA3Iiwic2VydmljZVByb3ZpZG9yU2hvcnROYW1lIjoi5bmz5Y-w5rWL6K-VIn0.gRul1yTzkWqwh3IJ_5NsrhUtZI-6dFZKPosaiDvggpg"\
 ,"IsInsideIP":true}; zg_7f25a4228a45471ca7d63149703b61ea=%7B%22sid%22%3A%201534244273925%2C%22updated%22%3A%201534244\
 809930%2C%22info%22%3A%201534244388892%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%\
 2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22account%2Faccount%3A149812027967\
 2%22%2C%22landHref%22%3A%20%22http%3A%2F%2Fwww.smarteoc.com%2F%23%2Falarm%2Funhandle%3F_k%3Dvomi6b%22%7D'}
response = requests.post(url, data=data, headers=headers)
print(response.text)
print(response.status_code)
