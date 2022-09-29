class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.age = age
        self.lastname = lastname

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')


x = Person('Edy', 'Stan', 20)
x.talk()
