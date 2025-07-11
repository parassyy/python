str1="paras suhas yadav"
a=str1.split()
b=[]
for i in a:
    b.append(i[::-1])
str2=" ".join(b)
print(str1)
print(str2)
