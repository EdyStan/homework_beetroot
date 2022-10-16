class TypeDecorators:

    @staticmethod
    def to_type(type_):
        def decorator(func):
            def wraps(*args):
                try:
                    return type_(func(*args))
                except SystemError as e:
                    raise e

            return wraps

        return decorator


@TypeDecorators.to_type(int)
def do_nothing(value):
    return value


@TypeDecorators.to_type(bool)
def do_something(value):
    value = str(value)
    return value
