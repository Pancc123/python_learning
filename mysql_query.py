#-*- coding:utf-8 -*-
from mysql_db import *
import os
import re
#method 1# 直接给出连接参数
'''host = 'mysql.test.hzzh.xyz'
username = 'cms'
password = 'Cms123'
db_name = 'iotplatform_mot'


''' 
#method 2
# 从数据库配置文件SQLconfig.config读取连接参数
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
#print(base_dir)
#base_dir=base_dir.replace('\\', '/')
#print(base_dir)
base_dir = base_dir+'/'+'SQLconfig.config'
print(base_dir)
config = getSQLCONFIG(r'D:/python_work/SQLconfig.config','Database1')
host = config[1]
username = config[2]
password= config[3]
db_name = config[0]
#db_name=db_name.strip('')
#password=password.strip('')
#username=username.strip('')
#host=host.strip('')
username=username.replace("'","")
password=password.replace("'","")
db_name=db_name.replace("'","")
host=host.replace("'","")



def query_database(db,sql):
    #conn1 = DB().conn('mysql.test.hzzh.xyz','cms','Cms123','iotplatform_mot',charset = 'utf8')
    #MYSQLdb.connect('IP','username','password','db_name','字符类型')
    with db.conn.cursor() as cursor:
        cursor.execute(sql)
    #data = cusor.fetchone()
    data = cursor.fetchall()
    # 获取MYSQL里的数据字段
    #fields = cursor.description
    print(data)
    #print(fields)
    db.close()
    return data


if __name__ == '__main__':
    db = DB(host, username, password, db_name)
    sql= "select metric_code,name  from t_point where id in (9939874034764175,11071531548810607,12084541227803443)"
    query_database(db,sql)
