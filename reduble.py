a=[1,2,2,3,2,4,2,5,2,6,2,7,2]
b=[]
for val in a:
    if val not in b:
        b.append(val)
print(a)
print(b)
