import sys

# Default path
print(sys.path)

# Append new path to the existing one
sys.path.append('/home/edystan/Desktop/folderul_D/courses/beetroot_academy/homework/18_modules-and-standard-lib/task_1')
print(sys.path)

# Define the entire path
sys.path = '/home/edystan/Desktop/folderul_D/courses/beetroot_academy/homework/18_modules-and-standard-lib/task_1'
print(sys.path)

try:
    import numpy
except SystemError:
    print('Works!')

# Though, why can numpy be imported even with the path changed?
