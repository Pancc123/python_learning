# -*- coding:utf-8 -*-
import os,sqlite3
db_file=os.path.join(os.path.dirname('/root/packages.tar.gz'),'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)
	
'''#初始化数据
conn=sqlite3.connect(db_file)
cursor=conn.cursor()
cursor.execute('create table user3(id varchar(20) primary key,name varchar(20) not null,score int)')
cursor.execute(r"insert into user3 values('A-001','panchengcheng','87')")
cursor.execute(r"insert into user3 values('A-002','panchengcheng','62')")
cursor.execute(r"insert into user3 values('A-003','panchengcheng','78')")
cursor.close()
conn.commit()
conn.close()'''

'''def get_score_in(low,high):
	conn=sqlite3.connect('/root/test.db')
	cursor=conn.cursor()
	cursor.execute('select score from user2 ')
	values=fetchall()
	t=values.sort()
	while True:
	  m=t.pop()
	  if m in range(low,high):
		  print(m)'''
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user2(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user2 values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user2 values ('A-004', 'Adam1', 85)")
cursor.execute(r"insert into user2 values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user2 values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select name from user2 where score>=? and score<=? ORDER BY score', (low, high))
    values = cursor.fetchall()
    print(values)
    i = len(values)
    print(i)
    L = []
    while i-1>=0:
        L.append(values[i-1][0])
        i = i-1
    L.reverse()
    return L
    cursor.close()
    conn.close()
m=get_score_in(60,90)
print(m)
