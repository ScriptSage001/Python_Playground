### := is called the "Walrus" operator - Officially called the "Assignment Expressions" operator
from operator import index


# if (n := len([1, 2, 3, 4, 5, 6])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")


### Typed Variable

# from typing import List, Tuple, Union, Dict
#
# number : int = 5
# name : str = "John"
#
# def sum(a: int, b: int) -> int:
#     return a + b
#
# list_numbers: List[int] = [1, 2, 3, 4, 5]
# name_age: Tuple[str, int] = ("John", 25)
# name_age_dict: Dict[str, int] = {"John": 25, "Jane": 30}
#
# mixed_holding_type: Union[str, int] = "John25"
# mixed_holding_type = "123425"


### Match Case

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

# print('200:', http_status(200))
# print('400:', http_status(400))
# print('404:', http_status(404))
# print('500:', http_status(500))
# print('503:', http_status(503))

### Dictionary Merge

# dict1 = {"name": "John", "age": 25}
# dict2 = {"city": "New York", "country": "USA"}
#
# merged_dict = dict1 | dict2
#
# print(merged_dict)

### Dictionary Update

# dict1 = {"name": "John", "age": 25}
# dict2 = {"city": "New York", "country": "USA"}
#
# print('dict1 before update:', dict1)
# dict1 |= dict2
# print('dict1 after update:', dict1)


### Multiple Context Manager

# with (
#     open('text.txt', 'r') as file1,
#     open('text_file.txt', 'r') as file2
# ):
#     print('File1:\n', file1.read(), end='\n\n')
#     print('File2:\n', file2.read(), end='\n\n')


### Exception Handling

# try:
#     a = int(input("Enter a number: "))
#     print('You entered:', a)
#
# except ValueError:
#     print("Invalid input! Please enter a number.")
#
# except Exception as e:
#     print("Something went wrong! Exception:", e)


### Raising Exception

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
#
# if b == 0:
#     raise ZeroDivisionError("Cannot divide by zero!")
#
# print(f"{a} / {b} = {a / b}")


### Try with Else

# try:
#     a = int(input("Enter a number: "))
#     print('You entered:', a)
#
# except ValueError:
#     print("Invalid input! Please enter a number.")
#
# except Exception as e:
#     print("Something went wrong! Exception:", e)
#
# else:
#     print("No exception occurred.")


### Try with Finally

# try:
#     a = int(input("Enter a number: "))
#     print('You entered:', a)
#
# except ValueError:
#     print("Invalid input! Please enter a number.")
#
# except Exception as e:
#     print("Something went wrong! Exception:", e)
#
# finally:
#     print("It's inside the finally block.")


### If __Name__ == "__Main__"

# from test_module import any_function


### Global and Local Variables

# x = 3
# def func():
#     x = 5
#     print(x)
#
# func()
# print(x)

# x = 3
# def func():
#     global x
#     x = 5
#     print(x)
#
# func()
# print(x)



### Enumerate

lst = ["John", "Jane", "Doe"]

# index = 0
# for item in lst:
#     print(f'Item at index {index} is {item}')
#     index += 1

# for index, item in enumerate(lst):
#     print(f'Item at index {index} is {item}')


### List Comprehensions

lst = [1, 2, 3, 4, 5]

# squaredList = []
# for item in lst:
#     squaredList.append(item ** 2)
# print(squaredList)

# squaredList = [i ** 2 for i in list]
# print(squaredList)


### Lamda Function

# def square(x):
#     return x*x
#
# print(square(5))

# square = lambda x: x*x
# print(square(5))


### Join Function

# list = ["John", "Jane", "Doe"]
# print('-'.join(list))


### Format

# sample_string = "Hello, my name is {0} and I am {1} years old."
# sample_string = sample_string.format("John", 25)
# print(sample_string)


### Map Function

# lst = [1, 2, 3, 4, 5]
# square = lambda x: x*x
#
# squared_list = map(square, lst)
# print(list(squared_list))

### Filter Function

# def even(x):
#     return x % 2 == 0
#
# lst = [1, 2, 3, 4, 5]
#
# print(list(filter(even, lst)))


### Reduce Function

# from functools import reduce
#
# sum = lambda x, y: x + y
# mul = lambda x, y: x * y
#
# lst = [1, 2, 3, 4, 5]
# print(reduce(sum, lst))
# print(reduce(mul, lst))