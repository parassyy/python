import csv

fobj=open("paras.csv""r")
robj=csv.readeer(fobj)
for row in robj:
    print(row)
    
fobj.close()
