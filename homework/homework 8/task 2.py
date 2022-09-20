"""
Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns
the value of squared a divided by b, construct a try-except block which raises an exception if the two values given
by the input function were not numbers, and if value b was zero (cannot divide by zero).
"""


def write_numbers():
    a = input('Write any number: ')
    b = input('Write any number (except 0): ')
    return int(a) ** 2 / int(b)


try:
    write_numbers()
except ValueError:
    print('Write an int pls!')
except ZeroDivisionError:
    print('The second int shouldn\'t be 0!!!')
