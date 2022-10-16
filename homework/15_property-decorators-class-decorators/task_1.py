import re


def validate(e_name):
    return re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', e_name)


class EmailStorage:

    def __init__(self, e_name):
        if not validate(e_name):
            raise SyntaxError('Your email is not good')
        self.e_name = e_name


rabla = EmailStorage('aedysss.777@gmail.com')
