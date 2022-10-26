# Let’s play with recursion. Make a function with argument index: int - call itself with index + 1. Create an if
# statement, before recursion call, like index < 10, to no get recursion exception.

def recursive_fct(my_int):
    if my_int < 10:
        my_int += 1
        print(my_int)
        recursive_fct(my_int)


recursive_fct(2)
