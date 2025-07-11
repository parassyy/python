def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

# 🔽 Taking input and using the function
number = int(input("Enter number: "))

if is_prime(number):
    print("This is a prime number")
else:
    print("This is not a prime number")
