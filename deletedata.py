from mysql.connector import connect

cn=connect(database="db1",
           user="root",
           password="system",
           host="localhost",
           port="3306")
c=cn.cursor()
rno=int(input("Rollno of std for delete:"))
cmd="delete from marks where rollno=%s"
c.execute(cmd,params=(rno,))
k=c.rowcount
if k>0:
    print("Student row is delete..")
else:
    print("Invalid rollno")
cn.commit()


