class calulate():
    def add(self,num1,num2):
        return num1+num2

cal=calulate()
a=int(input("enter the number num1:"))
b=int(input("enter the number num2:"))

re=cal.add(a,b)
print("the sum of num1 and num2 is:",re)
