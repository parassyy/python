num=int(input("enter the number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(f'{num} is Not Prime number')
            break
    else:
        print(f'{num} is Prime number')
