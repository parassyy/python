num=[54,65,98,78,21,36,5,48,74,54,35]
larg=num[0]
sec_lagr=num[0]
for i in range(len(num)):
    if num[i]>larg:
        larg=num[i]
for i in range(len(num)):
    if num[i]>sec_lagr and num[i]!=larg:
        sec_lagr=num[i]
print(sec_lagr)
