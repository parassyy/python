import mysql.connector

cn=mysql.connector.connect(database="db1",
                           user="root",
                           password="system",
                           host="localhost",
                           port="3306")
c=cn.cursor()
c.execute('''create table emp(
empno integer,
name varchar(20),
salary float(5))''')
print("table created...")
cn.close()
