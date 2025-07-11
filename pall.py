a=int(input('enter the number'))
s=0
temp=a
while temp>0:
    d=temp%10
    s+=d**3
    temp//=10
if a==s:
    print('pal')
else:
    print('not pal')
