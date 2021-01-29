# -*- coding:utf-8 -*-
from pymysql import connect,cursors
from pymysql.err import OperationalError
import configparser



testDB = {
    "host": "mysql.ynycloud.xyz",
    "user": "cms",
    "passwd": "Cms123",
    "port": 3306,
    "charset": "utf8"
}


# 执行sql
# db：数据库名称；sql：sql语句；testDB连接参数
def executeSQL(testDB,db, sql):
    """
    connect to database
    :return:
    """
    try:
        testDB["db"] = db
        config = testDB
        db = connect(**config)
        print("connect ok")
        # create cursor
        cursor = db.cursor()
        # print("Connect DB successfully!")
        cursor.execute(sql)
        # 获取所有数据
        data = cursor.fetchall()
        # print(data)
        return data
    except Exception as e:
        print(e)


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
        except OperationalError as e:
            print("Mysql error:%d %s" % (e.args[0], e.arg[1]))
        #self.cur = self.conn.cursor()

    def clear(self,table_name):
        #real_sql='truncate'+'table_name'+';'
        real_sql = 'delete'+table_name+';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0')
            cursor.execute(real_sql)
        self.cursor.commit()
        self.conn.close()

    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = 'insert into'+table_name+'('+key+')+VALUES+('+value+')'
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.cursor.commit()
        self.conn.close()

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
        self.conn.close()
        return data

    def close(self):
        self.conn.close()







