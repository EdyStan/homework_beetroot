# You need to transform the results of some function from a str type to an int type. Create a decorator for it.
# Advanced: create params for the decorator which will allow you to specify the final type.

def change_result_type(type_):
    def decorator_func(func):
        def wraps(*args):
            try:
                result = type_(func(*args))
                return result

            except TypeError:
                return None

        return wraps

    return decorator_func


@change_result_type('ddd')
def sum_(a, b):
    return str(a + b)


print(type(sum_(1, 2)))
