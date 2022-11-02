from task_3_classes import FractionClass

a = input('First fraction: (numerator / denominator) ')
b = input('Second fraction: (numerator / denominator) ')
x = FractionClass(a)
y = FractionClass(b)
print(f'Addition: {x + y}')
print(f'Subtraction: {x - y}')
print(f'Multiplication: {x * y}')
print(f'Division: {x / y}')

print(f'{x} < {y} is {x < y}')
print(f'{x} <= {y} is {x <= y}')
print(f'{x} > {y} is {x > y}')
print(f'{x} >= {y} is {x >= y}')
print(f'{x} != {y} is {x != y}')
print(f'{x} == {y} is {x == y}')
