# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 19:37:30 2025

@author: paras
"""

fobj=open("marks.txt","r")
while True:
    stud=fobj.readline()
    if stud=="":
        break
    print(stud,end="")
fobj.close()