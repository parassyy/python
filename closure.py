def outer(name):      # This is a closure function
    def inner():       # This is the inner function
                                    # This inner function can access the variable 'name' from the outer function
        print(f'Hello, {name}!')
    return inner
x=outer("Ashu")
x()  # This will print: Hello, Paras!