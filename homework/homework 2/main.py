name_1 = 'Edy'
day = 'Wednesday'

# task 1
"""
The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message
like this:
"Good day <name>! <day> is a perfect day to learn some python."
Note that <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string. 
"""

print(f'Good day {name_1}! {day} is a perfect day to learn some python.')

# task 2
"""
Manipulate strings.

Save your first and last name as separate variables, then use string concatenation to add them together with a white 
space in between and print a greeting.
"""
name_2 = 'Stan'
print(name_1 + ' ' + name_2)

# task 3
"""
Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 

    Addition
    Subtraction
    Division
    Multiplication
    Exponent (Power)
    Modulus
    Floor division
"""
a = -22
b = 3.14

print('Sum: ' + str(a + b) + '\nSubtraction: ' + str(a - b) + '\nDivision: ' + str(a/b) + '\nMultiplication: '
      + str(a*b) + '\nExponent: ' + str(b**a) + '\nModulus: ' + str(abs(a)) + '\nFloor division: ' + str(a//b))
