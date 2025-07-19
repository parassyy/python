from mysql.connector import connect

cn=connect(database="db1",
           user="root",
           password="system",
           host="localhost",
           port="3306")
c=cn.cursor()
c.execute("select *from marks")
s1=c.fetchone()
print(s1)
s2=c.fetchone()
print(s2)
c.execute("select *from marks")
while True:
    row=c.fetchone()
    if row==None:
        break
    print(row)
cn.close()
