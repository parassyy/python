# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 19:33:18 2025

@author: paras
"""
a1=open("file1.txt","r")
count=0
while True:
    ch=a1.read(1)
    if ch=="":
        break
    if ch in "aeiouAEIOU":
        count+=1
print(f'Count of vowels {count}')
a1.close()