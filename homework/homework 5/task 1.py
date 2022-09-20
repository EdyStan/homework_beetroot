"""
The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
"""

from random import sample

random_list = sample(range(1, 3000), 10)
x = 0
biggest_num = 0

while x < len(random_list):
    if random_list[x] > biggest_num:
        biggest_num = random_list[x]
    x += 1

print(random_list)
print(biggest_num)