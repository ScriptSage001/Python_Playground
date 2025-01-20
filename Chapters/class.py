class Student:
    id = '<Id>'
    name = '<Name>'
    grade = '<Grade>'

    # Constructor
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    # def set_info(self, id, name, grade):
    #     self.id = id
    #     self.name = name
    #     self.grade = grade

    def get_info(self):
        return self.id, self.name, self.grade

    @staticmethod
    def static_example():
        print("This is an example of a static method.")

ram = Student(1, 'Ram Davidson', 'C')
# ram.set_info(1, 'Ram Davidson', 'C')
print(ram.get_info())

ram.static_example()