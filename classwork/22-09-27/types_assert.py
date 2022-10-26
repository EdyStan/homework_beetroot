"""
Create a function where will be needed as an argument string_a and number_b. With using assert - be sure, that user
input arguments of this types. After it concatenate string_a with number_b
"""


def special_function(string_a, number_b):
    assert type(string_a) == str
    assert type(number_b) == int


special_function('dddd', 4)

print(isinstance(True, int))
print(type(True) == int)
