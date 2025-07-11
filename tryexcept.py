while True:
    try:
        n1=int(input("First number:"))
        n2=int(input("second number:"))
        n3=n1/n2
        print(f'division of {n1}/{n2}={n3}')
        break
    except ZeroDivisionError:
        print("cannot divide number with zero")

    except ValueError:
        print("input only integer values")
