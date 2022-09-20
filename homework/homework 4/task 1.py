"""
The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""
from random import randint

rand_num = str(randint(1, 10))
guess_num = input('Guess an int from 1 to 10: ')

if rand_num == guess_num:
    print(f'Congrats! The number is {rand_num}')
else:
    print(f'Wrong! The number was {rand_num}.')
