from mysql.connector import connect

cn=connect(database="db1",
           user="root",
           password="system",
           host="localhost",
           port="3306")
c=cn.cursor()
c.execute("select *from marks")
rows=c.fetchall()
print(rows)
cn.close()
