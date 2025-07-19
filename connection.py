import mysql.connector
cn=mysql.connector.connect(database="db1",
                           user="root",
                           password="system",
                           host="localhost",
                           port="3306")
print("connection established...")
print(cn)
cn.close()
