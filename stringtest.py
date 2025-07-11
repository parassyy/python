str1=input("enter the string")
a=str1.split()
b=[]
for i in a:
    b.append(i[::-1])
str2=" ".join(b)
print(str1)
print(str2)
