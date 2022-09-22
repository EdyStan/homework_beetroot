# Create list which will have 1000000 sorted numbers from 1 to 1000000 of any kind. After it, create a copy of this list and shuffle
# the values. After it, filter all odd elements, and measure, how much time it'll take for sorted and unsorted list.

from time import time
from copy import deepcopy
from random import shuffle

big_list = [i for i in range(1000000)]
shuffled_list = deepcopy(big_list)
shuffle(shuffled_list)

time_start_4 = time()
final = big_list[1::2]
print("First method ordered: ", time() - time_start_4)
#OR
time_start_1 = time()
final_shuffled_list = shuffled_list[1::2]
print("First method: ", time() - time_start_1)
#OR
time_start_2 = time()
shuffled_list_2 = [x for x in shuffled_list if x % 2]
print("Second method shuffled: ", time() - time_start_2)
#OR
time_start_3 = time()
shuffled_list_3 = [x for x in big_list if x % 2]
print("Second method ordered: ", time() - time_start_3)

