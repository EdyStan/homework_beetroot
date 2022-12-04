from generator import my_range

list_1 = [i for i in range(9, 1, -1)]
list_2 = [i for i in my_range(9, 1, -1)]

assert list_2 == list_1

list_3 = [i for i in range(1, 90, 4)]
list_4 = [i for i in my_range(1, 90, 4)]

assert list_3 == list_4

list_5 = [i for i in range(5, 5, 4)]
list_6 = [i for i in my_range(5, 5, 4)]

assert list_5 == list_6
