"""
User could input to you something. You'll to transform it to int and divide 1 by this number. Don't use if/else
blocks and print "Wrong input" in case if some exception happen
"""
n = input('Type an int: ')
try:
    1/int(n)
except (ZeroDivisionError, ValueError):
    print('Wrong input!')
