num=int(input("Enter a number: "))
s=0
while num>0:
    d=num%10
    s+=d
    num//=10
print("Sum of digits:", s)

#https://github.com/parassyy/python.git