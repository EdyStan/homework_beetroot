from random import sample
my_string = input('type whatever you want: ')

a = ''.join(sample(my_string, len(my_string)))
print(a)
