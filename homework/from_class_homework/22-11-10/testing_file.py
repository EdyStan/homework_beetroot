from debug_others_code import Employee, ListOfEmployees

e1 = Employee('Alfred', 45, 'regular employee', 20)
e1.start_working()
e1.finish_working()
print(e1.calculate_salary(), e1.name)

l1 = ListOfEmployees()
e2 = l1.add_employee()
l1.list_of_employees = e1
print(l1.list_of_employees)
del l1.list_of_employees
print(l1.list_of_employees)

for employee in l1:
    print(employee)

del l1.list_of_employees
print(l1.list_of_employees)

