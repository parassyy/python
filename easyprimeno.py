num=int(input("enter the number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("is not prime")
            break
    else:
        print(f'{num}it is prime number')
