# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    def __init__(self, name, language, experience):
        self.name = name
        self.language = language
        self.experience = experience

    def get_info(self):
        return f"{self.name} | {self.language} | {self.experience}"

def execute_question_one():
    ram = Programmer("RAM", "C#", 9)
    print(ram.get_info())

# execute_question_one()

# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:

    @staticmethod
    def square(number):
        return number ** 2

    @staticmethod
    def cube(number):
        return number ** 3

    @staticmethod
    def square_root(number):
        return number ** 0.5

def execute_question_two():
    number = 2
    print(f'Square of the numer {number} = {Calculator.square(number)}')
    print(f'Cube of the numer {number} = {Calculator.cube(number)}')
    print(f'Square Root of the numer {number} = {Calculator.square_root(number)}')

# execute_question_two()

# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’.
# Does this change the class attribute?

class TestClass:
    a = 'a' # class atribute

def execute_question_three():
    test = TestClass()
    test.a = 0 # instance attribute

    ### This doest not change the class attribute

# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator2_0:

    @staticmethod
    def square(number):
        return number ** 2

    @staticmethod
    def cube(number):
        return number ** 3

    @staticmethod
    def square_root(number):
        return number ** 0.5

    @staticmethod
    def greet():
        print("Welcome to the Calculator!")

def execute_question_four():
    number = 2
    Calculator2_0.greet()
    print(f'Square of the numer {number} = {Calculator2_0.square(number)}')
    print(f'Cube of the numer {number} = {Calculator2_0.cube(number)}')
    print(f'Square Root of the numer {number} = {Calculator2_0.square_root(number)}')

# execute_question_four()

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and
# get fare information of train running under Indian Railways.

class Train:

    def __init__(self):
        self.seat_data = {}
        self.seat_fare = {}

        for i in range(1, 51):
            self.seat_data.update({str(i): 'Available'})

        for i in range(1, 51):
            if i % 2 == 0:
                self.seat_fare.update({str(i): 1000})
            else:
                self.seat_fare.update({str(i): 900})

    def book_seats(self, name, seat_no):
        if seat_no not in self.seat_data.keys():
            return 'Invalid seat no.'
        self.seat_data[seat_no] = 'Reserved'
        return f'Seat no {seat_no} reserved successfully under the name {name}'

    def get_status(self, seat_no):
        if seat_no not in self.seat_data.keys():
            return 'Invalid seat no.'

        return f'Status of the seat no {seat_no} is {self.seat_data[seat_no]}'

    def get_fare(self, seat_no):
        if seat_no not in self.seat_fare.keys():
            return 'Invalid seat no.'

        return f'Fare for the seat no {seat_no} is {self.seat_fare[seat_no]}'


def execute_question_five():
    print('Welcome to the Indian Railways')
    train = Train()

    # Fare Inquiry
    print(train.get_fare('29'))
    print(train.get_fare('30'))

    # Book Seat
    res = train.book_seats('ScriptSage', '29')
    print(res)

    # Get Status
    print(train.get_status('29'))
    print(train.get_status('30'))

# execute_question_five()

# 6. Can you change the self-parameter inside a class to something else (say “sage”).
# Try changing self to “slf” or “harry” and see the effects.

class Test2:
    def __init__(slf): # We can do this, but this is not a good practice
        slf.test_data = 'Test Test'

def execute_question_six():
    test2 = Test2()
    print(test2.test_data)

# execute_question_six()