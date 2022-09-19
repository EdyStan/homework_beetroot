values = ['one', 'two', 'three', 'four', 'five']
my_list = [1, 3, 5]

for index in range(len(my_list)):
    values.remove(values[index])
    print(index, values)

print(values)