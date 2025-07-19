num=int(input("Enter the number:"))
s=0
temp=num
while temp>0:
    d=temp%10
    s+=d**3
    temp//=10

if s==num:
    print(num,"is armstrong")
else:
    print(num,"is not armstrong ")
