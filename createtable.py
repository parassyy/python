import mysql.connector
cn=mysql.connector.connect(database="db1",
                           user="root",
                           password="system",
                           host="localhost",
                           port="3306")
c=cn.cursor()
c.execute('''create table marks(
rollno integer,
name varchar(20),
sub1 float(5,2),
sub2 float(5,2),
total float(7,2),
avg float(5,2))''')
print("table created...")
cn.close()
