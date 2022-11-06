from datetime import datetime, timedelta


class Animal:

    def __init__(self, kind, name, age):

        self.kind = kind
        self.name = name
        self.age = age

    def __str__(self):
        return 'This is a {} named {} {} years old'.format(
                                                        self.kind,
                                                        self.name,
                                                        self.age)

    def __repr__(self):
        return 'Animal("{}", "{}", {})'.format(
                                            self.kind,
                                            self.name,
                                            self.age)

    @classmethod
    def dog(cls):
        name = input('Your dog name is ')
        age = input('How old is it? ')
        size = input('Size of your dog: ')
        dog = cls('dog', name, age)
        dog.size = size
        return dog

    def get_vaccinated(self):
        if self.kind in ['dog', 'cat']:
            self.vaccination_date = datetime.now()
        else:
            print("We will not vaccinate your animal!")


    def is_vaccinated(self):
        try:
            if self.vaccination_date > datetime.now() - timedelta(days=365.25):
                print(f'Your {self.kind} is vaccinated')
            print(f'Your {self.kind} is not vaccinated!')
        except AttributeError:
            if self.kind in ['dog', 'cat']:
                print('Animal was never vaccinated. \nYou need to vaccinate it.')
            else:
                print(f'You don\'t need to vaccinate your {self.kind}')


if __name__ == '__main__':

    the_dog = Animal.dog()
    print(the_dog, the_dog.size)
    the_dog.get_vaccinated()
    print(the_dog.vaccination_date)

    the_humster = Animal('humster', 'Mike', 2)
    print(the_humster)
    the_humster.get_vaccinated()

    the_humster.is_vaccinated()
    the_dog.is_vaccinated()