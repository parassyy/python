import csv

fobj=open("paras.csv","a",newline="")
wobj=csv.writer(fobj)
while True:
    eno=int(input("EmployeeNO:"))
    ename=input("EmployeeName:")
    sal=float(input("EmployeeSalary:"))
    wobj.writerow([eno,ename,sal])
    ans=input("Add another employee:")
    if ans=="no":
        break
fobj.close()
