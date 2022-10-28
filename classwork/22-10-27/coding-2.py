"""
Coding 2. Create a function that takes a positive integer as its argument and returns the result
of multiplication of all positive integers less or equal to the given one. For example, if argument
is 5 return value will be equal to 120 (as result of calculation of the expression 1*2*3*4*5).
"""

from time import time


def get_time_of_execution(any_func):
    def wrap_function(*args):
        start_time = time()
        any_func(*args)
        print("The execution time is ", time() - start_time)
        return any_func(*args)
    return wrap_function


# first way
@get_time_of_execution
def calculate_factorial(num):
    factorial = 1
    for number in range(1, num + 1):
        factorial *= number
    return factorial


print(calculate_factorial(5))