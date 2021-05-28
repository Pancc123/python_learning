from pymysql.err import OperationalError
import configparser


def getSQLCONFIG(filename,database_conf):
    cf = configparser.ConfigParser()
    cf.clear()  # 读取前清除已读内容。若不清除，多次读取文件会出现非预期内容。
    cf.read(filename)  # 读取配置文件
    # 读取对应文件参数
    _dbname = cf.get(database_conf, 'db_name')
    _host = cf.get(database_conf, 'host')
    _user = cf.get(database_conf, 'username')
    _pwd = cf.get(database_conf, 'password')
    return _dbname, _host, _user, _pwd


def gethttpConifg(filename, http_conifg):
    cf = configparser.ConfigParser()
    cf.clear()  # 读取前清除已读内容。若不清除，多次读取文件会出现非预期内容。
    cf.read(filename)     # 读取配置文件
    # 读取对应文件参数
    _url = cf.get(http_conifg, 'base_url')
    _header = cf.get(http_conifg, 'header')
    _timeout = cf.get(http_conifg, 'timeout')
    _username = cf.get(http_conifg, 'username')
    _password = cf.get(http_conifg,'password')
    return _url, _header, _timeout, _username,_password


if __name__ == "__main__":
    data = gethttpConifg('http_config.ini', 'Http_config')
    print(data[0])


