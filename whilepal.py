i=int(input("enter the no:"))
s=0
temp=i
while temp>0:
    d=temp%10
    s+=d**3
    temp//=10
if i==s:
    print("pal")
else:
    print("not pal")
