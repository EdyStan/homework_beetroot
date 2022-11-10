"""
You have a first list like values = [“one”, “two”, “three”, “four”, “five”] and a second list indexes [1, 3, 5].
You need to remove elements from first list which have an indexes from a second.
"""

values = ['one', 'two', 'three', 'four', 'five', 'six']
my_list = [0, 5, 3, 1, 5]
my_list = set(my_list)
my_list = list(my_list)
my_list.sort()

for index in reversed(my_list):
    values.pop(index)
    print(values)

