import re


class EmailStorage:

    @staticmethod
    def validate(func):
        def wrap(e_name):
            if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', e_name):
                return func(e_name)
            else:
                raise SyntaxError('Your email is not good')

        return wrap

    @validate
    def __init__(self, e_name):
        self.e_name = e_name


rabla = EmailStorage('aedysss.777@gmail.com')
