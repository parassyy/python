def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*n
num=int(input("Enter the number:"))
fact(num)
print(f'Factorial of {num} is {fact(num)}')
