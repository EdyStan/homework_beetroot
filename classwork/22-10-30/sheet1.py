class GrandParent(object):
    age = 70


class Parent(GrandParent):
    hair_color = 'black'


class Child(Parent):
    height = 1.5


c1 = Child()
print(c1.age)
print(c1.hair_color)
print(c1.height)

c1.school_grade = 10
print(c1.school_grade)

# del c1.age
print(dir(c1))
