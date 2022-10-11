class Person:
    def __init__(self, age, first_name, last_name, py_years=0):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.py_years = py_years

    def one_more_py_year(self):
        if type(self.py_years) == int:
            self.py_years += 1
        else:
            raise TypeError

    def aging(self):
        self.age += 1


class Student(Person):
    def __init__(self, age, first_name, last_name, py_years=0):
        super().__init__(age, first_name, last_name, py_years)
        self.nickname = None

    def set_nickname(self):
        self.nickname = input(f'What\'s the nickname of {self.first_name}?\n')


class Teacher(Person):
    def __init__(self, age, first_name, last_name, py_years=5):
        super().__init__(age, first_name, last_name, py_years)
        self.holiday = False

    def set_holiday(self):
        if not self.holiday:
            self.holiday = True
        else:
            self.holiday = False
