num=int(input("enter the number: "))
s=0
temp=num
while temp>0:
    digit=temp%10
    s+=digit**3
    temp//=10
if s==num:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")