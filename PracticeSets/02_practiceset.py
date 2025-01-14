# 1. Write a python program to add two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The first number is: ", num1)
print("The second number is: ", num2)
print("The sum of the two numbers is = ", num1 + num2)

# 2. Write a python program to find remainder when a number is divided by z.
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

print("The dividend and the divisor are: ", dividend, divisor)
print("The remainder of the dividend is: ", dividend % divisor)

# 3. Check the type of variable assigned using input () function.
variable = input("Enter anything: ")
print("The type of the input variable is: ", type(variable))

# 4. Use comparison operator to find out whether a given variable 'a' is greater than ‘b’ or not. Take a = 34 and b = 80
a = 34
b = 80
print("Is", a, "grater than", b, "? :", a > b)

# 5. Write a python program to find an average of two numbers entered by the user.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("The two numbers you have entered are: ",num1, num2)
print("The average of", num1, "and", num2, "is:", (num1 + num2)/2)

# 6. Write a python program to calculate the square of a number entered by the user.
num = int(input("Enter a number: "))
print("The square of the number is:", num**2)