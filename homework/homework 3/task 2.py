"""
The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. The program should check that the
string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the
outcome of the string evaluation.
"""

phone_num = '0728116655'

if phone_num.isnumeric() is True and len(phone_num) == 10:
    print('This could be a phone number')
else:
    print('This can\'t be a phone number')
