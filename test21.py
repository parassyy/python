num=int(input("enter the number:"))
s=0
temp=num
while temp>0:
    d=temp%10
    s+=d**4
    temp//=10
if num==s:
    print("is it armstrong")
else:
    print("is not armstrong")
