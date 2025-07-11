def fun1():
    x=100
    def fun2():
        y=200
        print(x)
        print(y)
        def fun3():
            x=400
            print(x)
        def fun4():
            nonlocal x
            x=500
        fun2()
        fun3()
        fun4()
        print(x)
fun1()
