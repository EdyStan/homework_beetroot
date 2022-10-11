class Animal:
    def talk(self):
        raise NotImplementedError("Must be implemented by a subclass")


class Dog(Animal):
    def talk(self):
        print('\"Romanian Dog\": Ham Ham!')


class Cat(Animal):
    def talk(self):
        print('Meow!')
