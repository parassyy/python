a=[10,21,36,45,65,78,99,44,22,11,33,36,48]
ec=0
od=0
for i in range(len(a)):
    if a[i]%2==0:
        ec+=1
    else:
        od+=1
print(a)
print(f'even count{ec}')
print(f'odd cound{od}')
