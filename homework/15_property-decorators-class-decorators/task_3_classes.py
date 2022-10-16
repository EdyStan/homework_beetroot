class TypeDecorators:

    @staticmethod
    def to_int(func):
        def wraps(*args):
            try:
                return int(func(*args))
            except SystemError as e:
                raise e

        return wraps

    @staticmethod
    def to_str(func):
        def wraps(*args):
            try:
                return str(func(*args))
            except SystemError as e:
                raise e

        return wraps

    @staticmethod
    def to_bool(func):
        def wraps(*args):
            try:
                return bool(func(*args))
            except SystemError as e:
                raise e

        return wraps

    @staticmethod
    def to_float(func):
        def wraps(*args):
            try:
                return float(func(*args))
            except SystemError as e:
                raise e

        return wraps


@TypeDecorators.to_int
def do_nothing(value):
    return value


@TypeDecorators.to_bool
def do_something(value):
    value = str(value)
    return value
