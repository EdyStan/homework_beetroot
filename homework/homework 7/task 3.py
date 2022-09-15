def make_operation(operation, *args):
    if operation == '+':
        the_sum = 0
        for i in args:
            the_sum += i
        return the_sum
    elif operation == "-":
        low = args[0]
        for i in args[1:-1]:
            low -= i
        return low
    elif operation == "*":
        the_multiplication = 1
        for i in args:
            the_multiplication *= i
        return the_multiplication
    else:
        print("Wrong operation!")


result = make_operation("-", 4, 6, 7, 8)
print(result)
