num=int(input("enter the number:"))
if num<=1:
    print("not a prime number")
else:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print("prime number")
    else:
        print("not prime number")
