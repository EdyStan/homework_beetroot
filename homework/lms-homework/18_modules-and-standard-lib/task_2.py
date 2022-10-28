import sys

# Default path
print(sys.path)

# Append new path to the existing one
sys.path.append('/homework/lms-homework/18_modules-and-standard-lib/task_1')
print(sys.path)

# Define the entire path
sys.path = '/homework/lms-homework/18_modules-and-standard-lib/task_1'
print(sys.path)

try:
    import numpy
except SystemError:
    print('Works!')

# Though, why can numpy be imported even with the path changed?
