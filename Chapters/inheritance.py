class Employee:
    company = 'Google'
    name = '<NAME>'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'The name is {self.name} and the company is {self.company}')


# class Programmer:
#     company = 'Meta'
#     name = '<NAME>'
#
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(f'The name is {self.name} and the company is {self.company}')

class Programmer(Employee):

    language = '<Lang>'

    def set_language(self, language):
        self.language = language

    def show(self):
        print(f'The name is {self.name}, the company is {self.company} and the language is {self.language}')



emp = Employee('Ram')
emp.show()

programmer = Programmer('ScriptSage')
programmer.set_language('Python')
programmer.show()