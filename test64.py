num=int(input("enter the number:"))
def countd(n):
    if n==0:
        print("Done!")
    else:
        print(n)
        countd(n-1)

x=countd(num)
print(x)
