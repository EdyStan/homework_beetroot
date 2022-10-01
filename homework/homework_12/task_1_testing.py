from task_1_classes import Cat, Dog

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
