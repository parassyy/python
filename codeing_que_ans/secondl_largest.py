#find the second largest number from the given listss


num=[12,23,45,67,10,20]
larg=num[0]
sec_larg=num[0]
for i in range(len(num)):
    if num[i]>larg:
        larg=num[i]
for i in range(len(num)):
    if num[i]>sec_larg and num[i]!=larg:
        sec_larg=num[i]
print(f'The second largest no from list is:{sec_larg}')
