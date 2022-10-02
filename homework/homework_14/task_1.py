def logger(func):
    def wrapper(*args):
        print(func.__code__.co_name + ' called with ' + f'{args}')
        return add
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(5, 2)

square_all(5, 66, 7, 8)
