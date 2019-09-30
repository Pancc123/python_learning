
import sqlite3

conn = sqlite3.connect('/home/pan/mqtt.db')

print ("Opened database successfully")

c = conn.cursor()

c.execute("delete from DTU_TRANS_FAIL;")
conn.commit()

c.execute("VACUUM DTU_TRANS_FAIL;")
conn.commit()

print ("del and vacumm successfully")
timestap=1504518961
for id in range(16132,2016163):
    val = (id,63050590572740283,1,1.0,0,timestap)
    strSql = "insert into DTU_TRANS_FAIL VALUES (?,?,?,?,?,?);"
    c.execute(strSql,val)
    conn.commit()
    timestap+=3
print("insert successfully")
conn.close()
