num=int(input('enter the number:'))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("is it not prime")
            break
    else:
        print('is it prime number')
