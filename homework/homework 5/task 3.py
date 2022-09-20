"""
Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but
not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration.
"""

def numbers(x, n):
    while x <= n:
        yield x
        x += 1


my_list = []
result_list = []

for i in numbers(1, 100):
    my_list.append(i)

print(my_list)

for j in my_list:
    if j % 7 == 0 and j % 5 != 0:
        result_list.append(j)

print(f'The wanted numbers are:\n{result_list}')
