num=int(input("enter the number:"))
s=0
temp=num
while temp>0:
    d=temp%10
    s=s+d**3
    temp=temp//10
if s==num:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")