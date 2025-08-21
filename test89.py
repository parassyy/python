for num in range(1, 1001):
    power = len(str(num))
    if num == sum(int(digit) ** power for digit in str(num)):
        print(num)
