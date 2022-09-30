def f1():
    local = None
    nana = 4
    rrr = 'fjdjdjjdjd'
    return 3


def f2(f):

    # https://www.codeguage.com/courses/python/functions-code-objects
    return f.__code__.co_nlocals


print(f2(f1))
