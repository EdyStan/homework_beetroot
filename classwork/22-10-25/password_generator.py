# Password Generator
#     1.    Password length should be from 4 to 16 symbols
#     2.    The following options should be available for the user:
# -  latin alphabet, upper case letters, lower case letters, punctuation symbols
# the response can be Y/N (possible usage y/n and Y/N)
#        3. Based on the given bass the password is generated randomly and given to the user

from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def password_generator():
    length = 0
    while length < 4 or length > 16:
        length = input('How long do you want the password to be? (4 - 16 characters): ')
        if length.isdigit():
            length = int(length)
        else:
            length = 0

    password_alphabet = ''
    sad_face = ':('

    def use_characters(characters, instance_words):
        while True:
            # The following command does not work if the input string is
            # f'Do you want to use {instance_words}?(y/n): '
            use_lowercase = input('Do you want to use ' + instance_words + '?(y/n): ')
            if use_lowercase == 'y':
                nonlocal password_alphabet
                password_alphabet += characters
                break
            elif use_lowercase == 'n':
                break
            else:
                nonlocal sad_face
                print('Please type y or n! ' + sad_face)
                sad_face += '('

    character_groups_list = [ascii_uppercase, ascii_lowercase, digits, punctuation]
    instance_words_list = ['uppercase letters', 'lowercase letters', 'digits', 'symbols']

    for character_group, varname in zip(character_groups_list, instance_words_list):
        use_characters(character_group, varname)

    password = ''.join(choices(password_alphabet, k=length))
    print(password)


password_generator()
