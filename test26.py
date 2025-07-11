num=[54,65,98,78,65,32,21]

small=num[0]
larg=num[0]
for i in num:
    if i>larg:
        larg=i
    if i<small:
        small=i
print(larg)
print(small)
