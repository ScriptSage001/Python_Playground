def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return num * factorial(num - 1)

n = int(input('Enter a number: '))
print(f'Factorial of the number {n} is: {factorial(n)}')