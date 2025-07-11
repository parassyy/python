def fun1():   #outer function
    x=100
    def fun2():  #inner function
        print(x)
    fun2()
def fun3():
    def fun4():
        x=200
        return x
    x=fun4()
    print(x)
fun1()
fun3()
