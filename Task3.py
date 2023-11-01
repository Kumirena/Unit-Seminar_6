class Person:
    def __init__(self, code, name):
        self.code = code
        self.name = name

class Student(Person):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.type = "Студент"

class Teacher(Person):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.type = "Преподаватель"