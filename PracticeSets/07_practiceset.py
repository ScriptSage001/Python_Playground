# 1. Write a program to print multiplication table of a given number using for loop.
from math import factorial

# n = int(input('Enter a number for multiplication table: '))
#
# for i in range(1, 11):
#     print(f'{n} * {i} = {n * i}', end='\n')

# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# l = ["Harry", "Soham", "Sachin", "Rahul"]
#
# for i in l:
#     if i.lower().startswith('s'):
#         print(f'Hi, Welcome {i}!')

# 3. Attempt problem 1 using while loop.

# n = int(input('Enter a number for multiplication table: '))
# i = 1
# while i <= 10:
#     print(f'{n} * {i} = {n * i}', end='\n')
#     i += 1

# 4. Write a program to find whether a given number is prime or not.

# n = int(input('Enter a number: '))
#
# for i in range(2, n):
#     if n % i == 0:
#         print('Number is not prime.')
#         break
# else:
#     print('Number is prime.')

# 5. Write a program to find the sum of first n natural numbers using while loop.

# n = int(input('Enter a number: '))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.

# n = int(input('Enter a number: '))
# fact = 1
#
# for i in range(1, n + 1):
#     fact = fact * i
#
# print(fact)

# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

# n = int(input('Enter a number: '))
# for i in range(1, n + 1):
#     print(' '* (n-i), end='')
#     print('*'* (2*i - 1), end='')
#     print('')

# 8. Write a program to print the following star pattern:
# *
# **
# ***      for n = 3

# n = int(input('Enter a number: '))
# for i in range(1, n + 1):
#     print('*'* i, end='')
#     print('')

# 9. Write a program to print the following star pattern.
# * * *
# *   *   for n = 3
# * * *

# n = int(input('Enter a number: '))
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print('*'* n, end='')
#         print('')
#     else:
#         print('*', end='')
#         print(' '* (n-2), end='')
#         print('*', end='')
#         print('')

# 10. Write a program to print multiplication table of n using for loops in reversed order.

# n = int(input('Enter a number for reverse multiplication table: '))
#
# for i in range(1, 11):
#     print(f'{n} * {11 - i} = {n * (11 - i)}', end='\n')
