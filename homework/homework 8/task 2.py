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
