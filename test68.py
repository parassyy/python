def febo(n):
    a,b=0,1
    for i in range(n):
        print(a,end="\n")
        a,b=b,a+b

num=int(input("enter the number of term:"))
print(febo(num))
        
