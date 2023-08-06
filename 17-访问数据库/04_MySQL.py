import mysql.connector

username = input('Username: ')
password = input('Password: ')
conn = mysql.connector.connect(user=username, password=password, database='test')
cursor = conn.cursor()

cursor.execute('drop table user')
cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
conn.commit()
cursor.execute('select * from user where id = %s', ('1',))
print(cursor.fetchall())

cursor.close()
conn.close()



