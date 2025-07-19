from mysql.connector import connect

cn=connect(database="db1",
           user="root",
           password="system",
           host="localhost",
           port="3306")
c=cn.cursor()
c.execute("select *from marks")
rows=c.fetchall()
for row in rows:
    rno,name,s1,s2,tot,avg=row
    res="PASS" if s1>=40 and s2>=40 else "FAIL"
    print(f'{rno}\t{name}\t{s1}\t{s2}\t{tot}\t{avg}\t{res}')
    cn.close()
