"""
The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

"Hello <name>, on your next birthday you’ll be <age+1> years"
"""

name = input('Type your name: ')
age = input('Type your age: ')
age = int(age) + 1

print(f"Hello {name}, on your next birthday you’ll be {age} years")
