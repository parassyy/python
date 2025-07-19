# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 10:22:37 2025

@author: paras
"""

import csv 
fobj=open("product.csv","a",newline='')
dwobj=csv.DictWriter(fobj, fieldnames=['pname','price'])
dwobj.writeheader()
while True:
    pname=input("ProductName:")
    price=int(input("Price:"))
    prod={'pname':pname,'price':price}
    dwobj.writerow(prod)
    ans=input("add another product?")
    if ans=="no":
        break
fobj.close()