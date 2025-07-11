n=1000
while n<=9999:
    s=0
    n1=n
    while n1>0:
        d=n1%10
        s=s+(d**4)
        n1=n1//10
    if s==n:
        print(n)
    n=n+1
    
