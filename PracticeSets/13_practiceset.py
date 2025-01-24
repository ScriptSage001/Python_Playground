# 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

    # virtualenv env1
    # .\env1\Scripts\activate.ps1
    # pip install pandas
    # pip install pyjokes
    # pip freeze > requirements.txt
    # deactivate

    # virtualenv env2
    # .\env2\Scripts\activate.ps1
    # pip install -r requirements.txt


# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

def execute_problem2():
    name = input("Enter the name of the student: ")
    marks = input("Enter the marks of the student: ")
    phone_number = input("Enter the phone number of the student: ")
    print("The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone_number))

# execute_problem2()

# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

def execute_problem3():
    table = [7 * i for i in range(1, 11)]
    table_string = "\n".join([str(i) for i in table])
    print(table_string)

# execute_problem3()

# 4. Write a program to filter a list of numbers which are divisible by 5.

def execute_problem4():
    numbers = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    filtered_numbers = list(filter(lambda x: x % 5 == 0, numbers))
    print(filtered_numbers)

# execute_problem4()

# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

def execute_problem5():
    from functools import reduce
    numbers = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    max_number = reduce(lambda x, y: x if x > y else y, numbers)
    print(max_number)

# execute_problem5()

# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

    #  pip freeze > requirements.txt
    #  virtualenv env3
    #  .\env3\Scripts\activate.ps1
    #  pip install -r requirements.txt

# 7. Explore the ‘Flask’ module and create a web server using Flask & Python.

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# app.run()