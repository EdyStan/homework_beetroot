"""
Coding 1. Create a function that takes a list of integers as its argument and returns the biggest value from that list
without using Python's built-in functions “min” and “max” or sorting the list.
"""
from math import inf


def maximum_number(number_list: list):
    biggest_num = -inf
    for element in number_list:
        if element > biggest_num:
            biggest_num = element

    return biggest_num


print(maximum_number([-5, -2]))
