num=int(input("enter the number:"))
count=0
while num>0:
    num//=10
    count+=1
print(f' number of digits {count}')
