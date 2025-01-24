# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any of these files are not present,
# a message without exiting the program must be printed prompting the same.

def open_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File {file_name} not found")

def execute_problem1():
    open_file('1.txt')
    open_file('2.txt')
    open_file('3.txt')

# execute_problem1()

# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

def execute_problem2():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, value in enumerate(my_list):
        if index in [2, 4, 6]:
            print(value)

# execute_problem2()

# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

def execute_problem3():
    number = int(input("Enter a number: "))
    table = [number * i for i in range(1, 11)]
    print(table)

# execute_problem3()

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

def execute_problem4():
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(a/b)
    except ZeroDivisionError:
        print("Infinite")

# execute_problem4()

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

def execute_problem5():
    number = int(input("Enter a number: "))
    table = [number * i for i in range(1, 11)]
    with open('Tables.txt', 'a') as file:
            file.write(f"Table of {number}: {str(table)}\n")

# execute_problem5()