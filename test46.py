def arm(num):
    s=0
    temp=num
    n=len(str(num))
    while temp>0:
        d=temp%10
        s+=d**n
        temp//=10
    if s==num:
        print("it is armstrong")
    else:
        print("not armstong")
    
n=int(input("enter the number:"))
(arm(n))
