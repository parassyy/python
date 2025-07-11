try:
    print("inside try block")
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    c=a/b
    print(f'Division of {a}/{b}={c}')

except ValueError:
    print("inside except block")
    print("input only integer value")
finally:
    print("inside finally block")

print("Continue...")
