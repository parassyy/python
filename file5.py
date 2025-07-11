# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 19:39:56 2025

@author: paras
"""

fobj=open("marks.txt","r")
while True:
    stud=fobj.readline()
    if stud=="":
        break  
    
        rno,name,sub1,sub2,sub3=stud.split()
        total=int(sub1)+int(sub2)+int(sub3)
        avg=total/3
        res="PASS" if int(sub1)>40 and int(sub2)>=40 and int(sub3)>=40 else "FAIL"

 print('{rno}\t{name}\t{sub1}\t{sub2}\t{sub3}\t{total}\t{avg}\t{res}')
fobj.close()