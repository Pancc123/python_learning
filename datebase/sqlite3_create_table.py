import sqlite3
#连接sqlite3数据库
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('create table user (id varchar(20) primary key,name varchar(20) not null)')
cursor.execute('insert into user(id,name) values(\'1\',\'Michael\')')
t=cursor.rowcount
print(t)
cursor.close()
conn.commit()
conn.close()
