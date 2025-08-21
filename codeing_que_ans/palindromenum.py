num=int(input("enter any number"))
num1=num
rev=0
while num>0:
    d=num%10
    rev=(rev*10)+d
    num=num//10
if num1==rev:
    print("pal")
else:
    print("Not Pal")
    
