from mysql.connector import connect

cn=connect(database="db1",
           user="root",
           password="system",
           host="localhost",
           port="3306")
c=cn.cursor()
cmd1="update marks set total=sub1+sub2"
cmd2="update marks set avg=total/2"
c.execute(cmd1)
c.execute(cmd2)
print("total,avg is update...")
cn.commit()
cn.close()
