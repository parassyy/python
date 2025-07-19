# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 10:09:30 2025

@author: paras
"""

import csv

fobj=open("paras.csv","r")
robj=csv.reader(fobj)
for row in robj:
    print(row)
    
fobj.close()