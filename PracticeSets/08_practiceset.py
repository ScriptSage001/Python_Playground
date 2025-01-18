# 1. Write a program using functions to find greatest of three numbers.

def find_greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return 'eq'

def take_input_find_greatest():
    print('Program to find the greatest number')
    print('Enter three number separated by a space: ')
    a, b, c = map(int, input().split())

    res = find_greatest(a, b, c)

    if res == 'eq':
        print('The numbers are equal.')
    else:
        print('Greatest number is ', res)

# take_input_find_greatest()

# 2. Write a python program using function to convert Celsius to Fahrenheit.

def deg_c_to_f(deg_c):
    return ((deg_c * 9) / 5) + 32

def take_input_convert_deg_c_to_f():
    print('Program to convert degrees C to F')
    deg_c = int(input('Enter degrees C: '))
    f = deg_c_to_f(deg_c)
    print('The converted temperature is:', f)

# take_input_convert_deg_c_to_f()

# 3. How do you prevent a python print() function to print a new line at the end.

def auto_new_line_print_prevention():
    print('This prints a new line by default.')
    print('This one does not prints any new line.', end='')
    print('This should not be printed on new line.')

# auto_new_line_print_prevention()

# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sum_of_first_n_natural_numbers(n):
    if n < 1:
        return 0
    else:
        return n + sum_of_first_n_natural_numbers(n - 1)

def take_input_sum_first_n_natural_numbers():
    print('Program to calculate sum of first n natural numbers')
    n = int(input('Enter n: '))
    res = sum_of_first_n_natural_numbers(n)
#    res = the_better_approach_without_recursion(n)
    if res > 0:
        print('The sum of first n natural numbers is ', res)
    else:
        print('Entered n should be greater than 0')

def the_better_approach_without_recursion(n):
    if n < 1:
        return 0
    else:
        return (n * (n + 1)) / 2

# take_input_sum_first_n_natural_numbers()

# 5. Write a python function to print first n lines of the following pattern:
# ***
# **
# * - for n = 3

def print_reverse_star(n):
    for i in range(n):
        print('*'*(n - i), end='')
        print('')

# print_reverse_star(5)

# 6. Write a python function which converts inches to cms.

def inches_to_cms(inches):
    return inches * 2.54

def take_input_inches_to_cms():
    print('Program to convert inches to cms')
    inches = int(input('Enter inches: '))
    cms = inches_to_cms(inches)
    print(f'{inches} inch = {cms} cm')

# take_input_inches_to_cms()

# 7. Write a python function to remove a given word from a list and strip it at the same time.

def strip_and_remove(word_to_remove, input_list):
    return [item.strip() for item in input_list if item.strip() != word_to_remove]

def take_input_strip_and_remove():
    input_list = ["  apple  ", "banana", "  cherry  ", "apple", "  orange  "]
    print('Program to strip and remove words')
    print('This is the list of words:', input_list)
    word = input('Enter a word to remove from the list:')
    stripped = strip_and_remove(word, input_list)
    print(f'{word} removed from the list and the other elements are stripped: {stripped}')

# take_input_strip_and_remove()

# 8. Write a python function to print multiplication table of a given number.

def multiplication_table_generator(n):
    print('The multiplication table of:', n)
    for i in range(1, 11):
        print(f'{i} * {n} = {n * i}')

# multiplication_table_generator(4)