n=int(input("enter the value for it"))
a=0
b=1
next=b
c=1
while c<=n:
    print(next,end=' ')
    c+=1
    a,b=b,next
    next=a+b
print()
