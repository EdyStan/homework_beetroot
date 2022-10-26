# Create function which will shuffle a given list of items and return a shuffled list.

from random import sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sample(range(1, len(my_list) + 1), len(my_list)))

# a little wrong xD
