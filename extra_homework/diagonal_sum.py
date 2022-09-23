"""
1. Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal.
Accept the size of the square matrix and elements for each column separated with
a space (for every row) as input from the user.
Input the size of the matrix: 3
2 3 4
4 5 6
3 4 7
Sum of matrix primary diagonal:
14
"""

from random import *

n = input('Pls type the dimension of the n x n matrix: ')
za_sum = 0
the_matrix = [[]]

for i in range(int(n)):
    for j in range(int(n)):
        the_matrix[i].append(randint(1, 30))
        print(the_matrix[i][j], end=' ')
        if i == j:
            za_sum += the_matrix[i][j]
    the_matrix.append([])
    print('\n')

print(f"The sum is: {za_sum}")
