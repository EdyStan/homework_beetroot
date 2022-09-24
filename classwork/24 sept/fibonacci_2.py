# Create a fibonacci function, which will take from user input - number index in the sequence and will
# print a number under this index.

def new_fibonacci(n):
    a, b = 0, 1

    if n == 0:
        return 1
    for i in range(n):
        a, b = b, a + b
    return a


print(new_fibonacci(4))