from task_3_classes import FractionClass

a = input('First fraction: ')
b = input('Second fraction: ')
x = FractionClass(a)
y = FractionClass(b)
print(f'Addition: {x + y}')
print(f'Subtraction: {x - y}')
print(f'Multiplication: {x * y}')
print(f'Division: {x / y}')
