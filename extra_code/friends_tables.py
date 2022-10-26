"""
1. You have 3 tables for 3 persons. Under first - sits John, Marry, Steve, under second Lucie, Petya, Peter,
under third - Tom, Chris and Avril. Find all possible combinations in which you could combine theme under 3 tables
for 2 persons and one for 3 persons. But remember, that Steve and Peter - had a conflict, and Avril doesn't like John.
So find a way in which they'll  not sit at one table.
"""
from itertools import combinations

friends_nt = ['John', 'Marry', 'Steve', 'Lucie', 'Petya', 'Peter', 'Tom', 'Chris', 'Avril']
table_2 = []
table_3 = []
index_2 = 0
table_1 = list(combinations(friends_nt, 2))
print(table_1)

for index in range(len(table_1) - 1):
    if 'Steve' in table_1[index] and 'Peter' in table_1[index]:
        table_1.remove(table_1[index])
        print('done')
    elif 'Avril' in table_1[index] and 'John' in table_1[index]:

table_2 = table_1
for index_1 in range(len(table_1) - 1):
    while len(table_2) !=
        for index_2 in range(len(table_2)):
            if table_1[index_1][0] or table_1[index_1][1] in table_2[index_2]:
                print(table_2[index_2])
                table_2.remove(table_2[index_2])


