# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 18:52:09 2025

@author: paras
"""

fobj=open("marks.txt","a")
while True:
    rollno=input("RollNO:")
    name=input("Name")
    sub1=int(input("subject1 mark"))
    sub2=int(input("Subject2 mark"))
    sub3=int(input("Subject3 mark"))
    print(rollno,name,sub1,sub2,sub3,file=fobj)
    ans=input("Add another student?")
    if ans=="no":
        break
fobj.close()