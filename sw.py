num=int(input("enter the number:"))
s=0
while num>0:
    d=num%10
    s=s+d
    num=num//10

print("sum of digts",s)
