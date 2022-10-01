import task_3_classes as t3

a = input('First fraction: ')
b = input('Second fraction: ')
x = t3.FractionClass(a)
y = t3.FractionClass(b)
print(f'Addition: {x + y}')
print(f'Subtraction: {x - y}')
print(f'Multiplication: {x * y}')
print(f'Division: {x / y}')
