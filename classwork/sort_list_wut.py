"""
You have a first list like values = [“one”, “two”, “three”, “four”, “five”] and a second list indexes [1, 3, 5].
You need to remove elements from first list which have an indexes from a second.
"""

values = ['one', 'two', 'three', 'four', 'five']
my_list = [1, 3, 5]

for index in range(len(my_list)):
    values.remove(values[index])
    print(index, values)

print(values)