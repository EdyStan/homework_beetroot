# Create function which will shuffle a given list of items and return a shuffled list.

from random import randint


def shuffle(my_list):
    shuffled_list = []
    for i in range(len(my_list)):
        new_var = randint(0, len(my_list) - 1)
        shuffled_list.append(my_list.pop(new_var))

    return shuffled_list


print(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 44]))
