values = ['one', 'two', 'three', 'four', 'five', 'six']
my_list = [0, 5, 3, 1, 5]
my_list = set(my_list)
my_list = list(my_list)
my_list.sort()

for index in reversed(my_list):
    values.pop(index)
    print(values)
