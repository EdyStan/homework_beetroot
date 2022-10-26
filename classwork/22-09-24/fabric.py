# Create a “fabric” function that will take as first argument - string with arguments, like this “a, b”,
# as second argument - small piece of python code, as this “a + b”, and return - a function signature.

def fabric(arguments, execution):
    return eval(f'lambda {arguments}: {execution}')


lala = fabric('a, b', 'a*b')
print(lala(2, 3))

blabla = fabric('a', 'print(a)')
print(blabla('dwndfn'))
