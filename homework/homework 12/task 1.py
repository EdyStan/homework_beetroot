class Animal:
    def talk(self):
        raise NotImplementedError("Must be implemented by a subclass")


class Dog(Animal):
    def talk(self):
        print('\"Romanian Dog\": Ham Ham!')


class Cat(Animal):
    def talk(self):
        print('Meow!')


a = Cat()
b = Cat()
c = Dog()
d = Cat()
e = Dog()

list_of_animals = [a, b, c, d, e]


def animals_talk(a_list):
    for element in a_list:
        element.talk()


animals_talk(list_of_animals)
