def sum_d(n):
    if n==0:
        return 0
    else:
        return n%10+sum_d(n//10)

num=int(input("enter the number:"))
print(sum_d(num))
