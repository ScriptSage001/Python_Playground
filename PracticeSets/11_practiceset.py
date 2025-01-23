# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(f'The Vector is : {self.a}i + {self.b}j')

class ThreeDVector(TwoDVector):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    def show(self):
        print(f'The Vector is : {self.a}i + {self.b}j + {self.c}k')

def execute_problem_one():
    a = TwoDVector(1, 2)
    b = ThreeDVector(-9, 2, 3)

    a.show()
    b.show()

# execute_problem_one()

# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print('Bow Bow')

# 3. Create a class ‘Employee’ and add salary and increment properties to it.
    # Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
    # which changes the value of increment based on the salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.increment = 0

    @property
    def salary_after_increment(self):
        return self.salary + (self.salary * self.increment)/100

    @salary_after_increment.setter
    def salary_after_increment(self, value):
        self.increment = ((value / self.salary) - 1) * 100

def execute_problem_three():
    emp = Employee('John', 24100)
    print(emp.name, emp.salary, emp.increment)

    emp.salary_after_increment = 28000
    print(emp.name, emp.salary, emp.increment)

# execute_problem_three()

# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, realpart, imagpart):
        self.real = realpart
        self.imag = imagpart

    def __add__(self, other):
        return Complex((self.real + other.real), (self.imag + other.imag))

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.imag * other.real) + (self.real * other.imag)
        return Complex(real_part, imag_part)

    def __str__(self):
        return f'({self.real} + {self.imag}i)'

def execute_problem_four():
    complex1 = Complex(2, 3)
    complex2 = Complex(4, 5)

    print(complex1 + complex2)
    print(complex1 * complex2)

# execute_problem_four()

# 5. Write a class vector representing a vector of n dimensions.
# Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b, self.c + other.c)

    def __mul__(self, other):
        return Vector(self.a * other.a, self.b * other.b, self.c * other.c)

    def __str__(self):
        res = f'({self.a}i'

        if self.b < 0:
            res += f' - {self.b * (-1)}j'
        else:
            res += f' + {self.b}j'

        if self.c < 0:
            res += f' - {self.c * (-1)}k)'
        else:
            res += f' + {self.c}k)'

        return res

def execute_problem_five():
    vector1 = Vector(1, 2, -3)
    vector2 = Vector(4, -5, 6)

    print(f'Vector One: {vector1}')
    print(f'Vector Two: {vector2}')
    print(f'Vector1 + Vector2: {vector1 + vector2}')
    print(f'Vector1 * Vector2: {vector1 * vector2}')

# execute_problem_five()

# 6. Write __str__() method to print the vector as follows: 7i + 8j +10k
# Assume vector of dimension 3 for this problem.

# Already done in the Problem 5.

# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class VectorOverloaded:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        return VectorOverloaded(self.a + other.a, self.b + other.b, self.c + other.c)

    def __mul__(self, other):
        return VectorOverloaded(self.a * other.a, self.b * other.b, self.c * other.c)

    def __str__(self):
        res = f'({self.a}i'

        if self.b < 0:
            res += f' - {self.b * (-1)}j'
        else:
            res += f' + {self.b}j'

        if self.c < 0:
            res += f' - {self.c * (-1)}k)'
        else:
            res += f' + {self.c}k)'

        return res

    def __len__(self):
        return 3

def execute_problem_seven():
    vector = VectorOverloaded(1, 2, -3)

    print(f'The Vector: {vector}. Length: {len(vector)}')

# execute_problem_seven()

### Bonus - Dynamic Dimension Vector

class DynamicVector:
    def __init__(self, *components):
        self.components = list(components)

    def __add__(self, other):
        length = max(len(self.components), len(other.components))
        self_padded = self.components + [0] * (length - len(self.components))
        other_padded = other.components + [0] * (length - len(other.components))
        return DynamicVector(*[a + b for a, b in zip(self_padded, other_padded)])

    def __mul__(self, other):
        length = max(len(self.components), len(other.components))
        self_padded = self.components + [0] * (length - len(self.components))
        other_padded = other.components + [0] * (length - len(other.components))
        return DynamicVector(*[a * b for a, b in zip(self_padded, other_padded)])

    def __str__(self):
        res = ""
        for i, comp in enumerate(self.components):
            if comp < 0:
                res += f' - {abs(comp)}v{i+1}'
            else:
                if i == 0:  # First component
                    res += f'({comp}v{i+1}'
                else:
                    res += f' + {comp}v{i+1}'

        if self.components:
            res += ')'

        return res

    def __len__(self):
        return len(self.components)

def execute_problem_bonus():
    vector1 = DynamicVector(1, 2, -3, -2, 5)
    vector2 = DynamicVector(4, -5, 6)

    print(f'Vector1: {vector1}')
    print(f'Vector2: {vector2}')
    print(f'Vector1 + Vector2: {vector1 + vector2}')
    print(f'Vector1 * Vector2: {vector1 * vector2}')
    print(f'Length of Vector1: {len(vector1)}')

# execute_problem_bonus()