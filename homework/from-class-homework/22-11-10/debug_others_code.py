from datetime import datetime


class Employee:
    def __init__(self, name, age, position, salary_per_hour):
        self.__name = name
        self.__age = age
        self.__position = position
        self.__salary_per_hour = salary_per_hour
        self.__hours_worked = 0
        self.__started_pass = None

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f"Name: {self.__name}, hourly salary: {self.__salary_per_hour}"

    def start_working(self):
        self.__started_pass = datetime.now()

    def finish_working(self):
        if self.__started_pass is not None:
            difference = datetime.now() - self.__started_pass
            self.__hours_worked += difference.total_seconds() / 3600

    def calculate_salary(self):
        return self.__hours_worked * self.__salary_per_hour


class ListOfEmployees:
    def __init__(self):
        self.__list_of_employees = []
        self.__current_index = 0

    @property
    def list_of_employees(self):
        return self.__list_of_employees

    @list_of_employees.setter
    def list_of_employees(self, new_employee: Employee):
        self.__list_of_employees.append(new_employee)
        print(f'Welcome to our new employee, {new_employee.name}!')

    @list_of_employees.deleter
    def list_of_employees(self):
        print(f'Everybody say goodbye to {self.__list_of_employees[-1].name}')
        self.__list_of_employees.pop()

    @classmethod
    def add_employee(cls):
        name = input("What is your employee's name? ")
        age = int(input("What is your employee's age? "))
        position = input("What is your employee's position? ")
        salary_per_hour = input("What is your employee's hourly salary? ")
        print(f'Welcome to our new employee, {name}!')
        new_employee = Employee(name, age, position, salary_per_hour)
        cls.list_of_employees = new_employee
        return new_employee

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index < len(self.__list_of_employees):
            x = self.__list_of_employees[self.__current_index]
            self.__current_index += 1
            return x
        else:
            raise StopIteration

