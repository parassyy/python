a=[]
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("enter value"))
        row.append(value)
    a.append(row)
b=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(a[j][i])
    b.append(row)
print(a)
print(b)
