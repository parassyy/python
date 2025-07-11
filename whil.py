num=int(input('Enter any number'))
ec=0
oc=0
while num>0:
    d=num%10
    if d%2==0:
        ec+=1
    else:
        oc+=1
        num=num//10
print(f'Even Digits count {ec}')
print(f'Odd Digits count {oc}')
