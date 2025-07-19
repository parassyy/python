# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 10:37:26 2025

@author: paras
"""

import csv

fobj=open("product.csv","r")
drobj=csv.DictReader(fobj,fieldname=['pname','price'])
for row in drobj:
    print(row['pname'],row['price'])
fobj.close()