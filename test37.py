num=int(input('enter then number:'))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print('number not prime')
            break
    else:
        print("this is prime")
