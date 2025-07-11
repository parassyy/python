str1="4a3b2c1d"
str2=""
for i in range(0,len(str1),2):
    n=int(str1[i])
    ch=str1[i+1]
    str2=str2+(n*ch)
print(str1)
print(str2)
