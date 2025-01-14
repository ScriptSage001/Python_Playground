# 1. Write a program to store seven fruits in a list entered by the user.
fruits = []

f1 = input("Enter a fruit name: ")
fruits.append(f1)
f2 = input("Enter a fruit name: ")
fruits.append(f2)
f3 = input("Enter a fruit name: ")
fruits.append(f3)
f4 = input("Enter a fruit name: ")
fruits.append(f4)
f5 = input("Enter a fruit name: ")
fruits.append(f5)
f6 = input("Enter a fruit name: ")
fruits.append(f6)
f7 = input("Enter a fruit name: ")
fruits.append(f7)

print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
m1 = int(input("Enter the marks of student1: "))
m2 = int(input("Enter the marks of student2: "))
m3 = int(input("Enter the marks of student3: "))
m4 = int(input("Enter the marks of student4: "))
m5 = int(input("Enter the marks of student5: "))
m6 = int(input("Enter the marks of student6: "))

marks = [m1, m2, m3, m4, m5, m6]
marks.sort()

print(marks)

# 3. Check that a tuple type cannot be changed in python.
tup = (1, 2, 3)
print(tup)
tup[1] = 'Ram'
print(tup)

# 4. Write a program to sum a list with 4 numbers.
nums = [1, 2, 3, 4]
print(sum(nums))

# 5. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))

