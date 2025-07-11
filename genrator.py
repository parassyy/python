def fun1():
    return 1
    return 2
    return 3

def fun2():
    yield 1
    yield 2
    yield 3
    

x=fun1()
print(x)


y=fun2()
value1=next(y)
value2=next(y)
value3=next(y)
print(value1,value2,value3)

z=fun2()
for val in z:
    print(val)
