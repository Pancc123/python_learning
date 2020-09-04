# -*- coding:utf-8 -*-
from pymysql import connect,cursors
from pymysql.err import OperationalError
import configparser


def getSQLCONFIG(filename,database_conf):
    cf = configparser.ConfigParser()
    #读取配置文件
    cf.read(filename)
    #读取对应文件参数
    _dbname = cf.get(database_conf, 'db_name')
    _host = cf.get(database_conf, 'host')
    _user = cf.get(database_conf, 'username')
    _pwd = cf.get(database_conf, 'password')
    return _dbname, _host, _user, _pwd


class DB:
    def __init__(self, host, username, password, db_name):
        try:
            self.conn = connect(host, username, password, db_name, charset='utf8')
            '''config ={ 
                     host:host,
                     username=username,
                     password=password,
                     db_name=db_name,
                     charset='utf8'
                     }   
               self.conn = connect(**config)'''
        except OperationalError as e:
            print("Mysql error:%d %s" % (e.args[0], e.arg[1]))

    def clear(self,table_name):
        #real_sql='truncate'+'table_name'+';'
        real_sql = 'delete'+table_name+';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0')
            cursor.execute(real_sql)
        self.cursor.commit()

    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = 'insert into'+table_name+'('+key+')+VALUES+('+value+')'
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.cursor.commit()

    def query_database(self, sql):
        # conn1 = DB().conn('mysql.test.hzzh.xyz','cms','Cms123','iotplatform_mot',charset = 'utf8')
        # MYSQLdb.connect('IP','username','password','db_name','字符类型')
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        # data = cusor.fetchone()
        data = cursor.fetchall()
        # 获取MYSQL里的数据字段
        # fields = cursor.description
        print(data)
        # print(fields)
        return data

    def close(self):
        self.conn.close()







