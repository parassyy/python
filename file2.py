# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 19:26:28 2025

@author: paras
"""

fobj=open("file1.txt","r")
s1=fobj.read(1)
print(s1)


s2=fobj.read(5)
print(s2)

s3=fobj.read()
print(s3)