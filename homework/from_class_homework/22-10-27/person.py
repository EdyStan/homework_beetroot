class Person:
    def __init__(self, name, age, gender='undefined'):
        self._name = name
        self.__age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, answer):
        self._gender = answer

    @gender.deleter
    def gender(self):
        self._gender = 'undefined'

    def __hash__(self):
        return hash(self._name) ^ hash(self.__age)


class BusDriver(Person):
    def __init__(self, name, age, gender='undefined', years=5):
        super().__init__(name, age, gender)
        self._years_of_driving = years

    @property
    def years_of_driving(self):
        return self._years_of_driving

    @years_of_driving.setter
    def years_of_driving(self, years: float):
        self._years_of_driving += years


class Student(Person):
    def __init__(self, name, age, gender='undefined', credits_number=0, status='enrolled'):
        super().__init__(name, age, gender)
        self._credits = credits_number
        self._status = status

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, credits_gain):
        self._credits += credits_gain

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status: str):
        self._status = new_status


class Patient(Person):
    def __init__(self, name, age, gender='undefined', diagnostic='undefined'):
        super().__init__(name, age, gender)
        self._diagnostic = diagnostic

    @property
    def diagnostic(self):
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, affection):
        self._diagnostic = affection

    @diagnostic.deleter
    def diagnostic(self):
        self._diagnostic = 'undefined'

    def is_healthy(self):
        if self._diagnostic == 'undefined' or self._diagnostic == 'nothing':
            print('The patient is healthy.')
        else:
            print('The patient needs to be treated.')


p1 = Person('George', 22)

print(hash(p1))
p1.gender = 'male'
print(p1.gender)
print(hash(p1))  # Hash does not change when the gender is assigned to another value

print(p1.name)
p1._name = 'Andrew'
print(p1.name)

print(hash(p1))  # Hash changes with the change of the name

