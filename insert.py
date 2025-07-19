from mysql.connector import connect
cn=connect(database="db1",
           user="root",
           password="system",
           host="localhost",
           port="3306")
c=cn.cursor()
cmd='''insert into marks(rollno,name,sub1,sub2)values
(%s,%s,%s,%s)'''
while True:
    rno=int(input("rollno:"))
    name=input("student name:")
    sub1=int(input("sub1 marks:"))
    sub2=int(input("sub2 marks:"))
    c.execute(cmd,params=(rno,name,sub1,sub2))
    ans=input("add another student?")
    if ans=="no":
        cn.commit()
        break
cn.close()
