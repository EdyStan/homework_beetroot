import task_1_classes as t1

x = t1.Person(19, 'Alexander', 'Jipa')
print(x.age)
print(x.py_years)


y = t1.Student(15, 'Mathias', 'Szabo')
y.set_nickname()
y.aging()
print(y.age)


z = t1.Teacher(30, 'John', 'Mariella', 8)
z.one_more_py_year()
print(z.py_years)
print(z.holiday)
z.set_holiday()
print(z.holiday)