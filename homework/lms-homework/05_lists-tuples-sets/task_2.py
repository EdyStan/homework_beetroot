from random import sample

list_1 = sample(range(1, 20), 11)
list_2 = sample(range(1, 20), 11)
print(f'list 1:\n{list_1}\n\nlist2:\n{list_2}\n')

x = 0
my_set = set()

while x < len(list_1):
    if list_1[x] in list_2:
        my_set.add(list_1[x])
    x += 1

print(f'The final common numbers are:\n{my_set}')
