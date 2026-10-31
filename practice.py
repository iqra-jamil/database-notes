import sqlite3 as sq
# we can chk executemany () later
conn=sq.connect('mynewdatabase.db')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS students (name TEXT ,marks INTEGER ,email TEXT UNIQUE)')
conn.commit()

sql1=("iqra",90,"iqraj690@gmail.com")
sql2=("iqra2",98,"iqraj667@gmail.com" )
sql3=("iqra3",100,"iqraj2690@gmail.com" )
sql4=("junaid","junaid123@gmail.com","iqra2")
# cursor.execute('INSERT OR IGNORE INTO students  VALUES (?,?,? )',sql1)
listoftuples=[sql1,sql2,sql3]
# cursor.execute('INSERT OR IGNORE INTO students  VALUES (?,?,?)',sql2)
# cursor.execute('INSERT OR IGNORE INTO students  VALUES (?,?,?)',sql3)
# cursor.execute('UPDATE OR IGNORE students SET name=?,email=? WHERE name=?',sql4)
cmd1= 'INSERT OR IGNORE INTO students  VALUES (?,?,? )'

cmd4= 'UPDATE OR IGNORE students SET name=?,email=? WHERE name=?'
cursor.executemany(cmd1,listoftuples)
conn.commit()
cursor.execute('SELECT * FROM students');
res=cursor.fetchall()
print(res)
conn.close()

