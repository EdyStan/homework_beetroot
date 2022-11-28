# Use existing password generator function to generate passwords from 4 to 8 characters long that will contain only
# digits. Create a function that will try to guess generated password by brute force, e.g. continuously trying
# out all possible combinations of characters in the password. That mean that for only-digits password  of 4 characters
# length you potentially should try combinations from '0000', '0001', '0002' ... to ... '9999'. If guessed variant is
# equal to generated password - your brute force function will return its value. Then create (or find existing) time
# measurement decorator, decorate your brute force function with it and perform measurements of execution time for
# passwords of different length. Add results of measurements to your source file as a comment.

from random import randrange, choices
from string import digits


def timer(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start_time = perf_counter()
        fn(*args, **kwargs)
        end_time = perf_counter()
        return end_time - start_time

    return inner


def password_generator():
    while True:
        length = randrange(4, 9)
        password = ''.join(choices(digits, k=length))
        # repeat = input(f'Your password is: {password}\nDo you want to keep it?(y/n): ')
        # if repeat == 'y':
        #     return password
        print(password + f'\nof length {length}')
        return password


@timer
def hacking_function(password):
    password = str(password)
    if len(password) == 4:
        for num in range(0, 10000):
            if password == '{0:04}'.format(num):
                print('The account has been hacked!')
                return 0
    if len(password) == 5:
        for num in range(0, 100000):
            if password == '{0:05}'.format(num):
                print('The account has been hacked!')
                return 0
    if len(password) == 6:
        for num in range(0, 1000000):
            if password == '{0:06}'.format(num):
                print('The account has been hacked!')
                return 0
    if len(password) == 7:
        for num in range(0, 10000000):
            if password == '{0:07}'.format(num):
                print('The account has been hacked!')
                return 0
    if len(password) == 8:
        for num in range(0, 100000000):
            if password == '{0:08}'.format(num):
                print('The account has been hacked!')
                return 0


list_of_4 = []
list_of_5 = []
list_of_6 = []
list_of_7 = []
list_of_8 = []

for _ in range(100):
    i_dont_want_to_be_hacked = password_generator()
    if len(i_dont_want_to_be_hacked) == 4:
        list_of_4.append(hacking_function(i_dont_want_to_be_hacked))
    if len(i_dont_want_to_be_hacked) == 5:
        list_of_5.append(hacking_function(i_dont_want_to_be_hacked))
    if len(i_dont_want_to_be_hacked) == 6:
        list_of_6.append(hacking_function(i_dont_want_to_be_hacked))
    if len(i_dont_want_to_be_hacked) == 7:
        list_of_7.append(hacking_function(i_dont_want_to_be_hacked))
    if len(i_dont_want_to_be_hacked) == 8:
        list_of_8.append(hacking_function(i_dont_want_to_be_hacked))

# there, I was trying to make a graph
