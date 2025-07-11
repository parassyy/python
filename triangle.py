a=[]
print("input elements of the matrix")
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("enter the values"))
        row.append(value)
    a.append(row)
print("upper triangle")
for i in range(3):
    for j in range(3):
        if j>=i:
            print(a[i][j],end=' ' )
        else:
            print(' ',end=' ')
    print()
print()
print("lower triangle")
for i in range(3):
    for j in range(3):
        if j<=i:
            print(a[i][j],end=' ')
    print()
print()
print('matrix')
for i in range(3):
    for j in range(3):
        print(a[i][j],end=' ')
    print()
print()
