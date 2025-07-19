# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 09:58:42 2025

@author: paras
"""

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