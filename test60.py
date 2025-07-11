def is_prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
            return True
        else:
            return False
n=int(input("enter the number:"))
if is_prime(n):
    print("This is prime")
else:
    print("this is not prime")
