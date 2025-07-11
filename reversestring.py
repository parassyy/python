str1="pyhton java database"
a=str1.split()
b=[]
for s in a:
    b.append(s[::-1])
str2=" ".join(b)
print(str1)
print(str2)
