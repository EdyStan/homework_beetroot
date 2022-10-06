class EmailStorage:

    @staticmethod
    def validate(func):
        def wrap(name):
            if name != r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b':
                return func(name)

        return wrap

    @validate
    def __init__(self, e_name):
        self.e_name = e_name


rabla = EmailStorage('lalal')
print(rabla.e_name)