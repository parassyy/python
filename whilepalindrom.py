num=int(input("enter the number"))
temp=num
rev=0
while temp>0:
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10
if num==rev:
    print("palindrom")
else:
    print("not palindrom")
