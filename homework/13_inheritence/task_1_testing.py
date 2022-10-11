from task_1_classes import Person, Student, Teacher

x = Person(19, 'Alexander', 'Jipa')
print(x.age)
print(x.py_years)


y = Student(15, 'Mathias', 'Szabo')
y.set_nickname()
y.aging()
print(y.age)


z = Teacher(30, 'John', 'Mariella', 8)
z.one_more_py_year()
print(z.py_years)
print(z.holiday)
z.set_holiday()
print(z.holiday)
