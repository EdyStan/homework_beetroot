my_list = [1, 2, 44, 2, 4]
my_tuple = 4, 6, 7, 2, 0

# 1st task
max_item = max(my_list)
print(max_item)

# 2nd task
average = sum(my_tuple) / len(my_tuple)
print(average)

# 3rd task
reversed_list = []
index = len(my_list) - 1
while index > -1:
    reversed_list.append(my_list[index])
    index -= 1

print(reversed_list)

# 4th task
another_list = []
for i in range(len(my_list)):
    another_list.append(my_list[i])

print(another_list)
