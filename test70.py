def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*n

r=fact(5)
print(r)
