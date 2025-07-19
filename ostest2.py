import os

f=open("file10.txt","w")
f.write("HEllo")
f.close()
cwd=os.getcwd()
print(f'file is created in {cwd}')
