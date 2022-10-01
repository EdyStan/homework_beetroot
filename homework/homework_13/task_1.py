def f1():
    local = 33
    nana = 4
    rrr = 2
    return local + nana + rrr


def f2(f):
    return f.__code__.co_nlocals  # https://www.codeguage.com/courses/python/functions-code-objects


print(f2(f1))
