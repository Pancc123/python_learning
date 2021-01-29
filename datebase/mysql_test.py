# -*- coding:utf-8 -*-
from pymysql import cursors, connect

conn = connect(host='localhost', user='root', password='pan123',db='guest', charset='utf8mb4',
               cursorclass=cursors.DictCursor)
try:
    with conn.cursor() as cursor:

         sql = 'insert into sign_guest (realname, phone, email, sign, ' \
               'event_id, create_time) values ("Tom", 15067196993, "tom@mail.com", 0,1 ,NOW());'
         cursor.execute(sql)
    conn.commit()

    with conn.cursor() as cursor:

        sql= 'select realname,phone,email,sign from sign_guest where phone=%s'
        cursor.execute(sql, ('15067196993',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()

