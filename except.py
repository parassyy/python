import sys
while True:
    try:
        n1=int(input("enter first number:"))
        n2=int(input("enter second number:"))
        n3=n1/n2
        print(f'Division of {n1}/{n2}={n3}')
        break
    except:
        t=sys.exc_info()
        print(t[0])
        print(t[1])
