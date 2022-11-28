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
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return to_execute

    return inner


def password_generator():
    while True:
        length = randrange(4, 8)

        try:
            password = ''.join(choices(digits, k=length))
            repeat = input(f'Your password is: {password}\nDo you want to keep it?(y/n): ')
            if repeat == 'y':
                return password
        except IndexError:
            print('You have no characters to make a password. Try again accepting at least one set of characters!\n')


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


i_dont_want_to_be_hacked = password_generator()

hacking_function(i_dont_want_to_be_hacked)


