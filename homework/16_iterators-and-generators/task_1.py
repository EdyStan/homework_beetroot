def with_index(iterable, start=0):
    for elem in iterable:
        yield start, elem
        start += 1


cities = ['Jakarta', 'Sao Paulo', 'Lima', 'Washington DC']

list_1 = [element for index, element in with_index(cities) if index % 2 == 0]
list_2 = [element for index, element in enumerate(cities) if index % 2 == 0]

assert list_1 == list_2

for index, element in with_index(cities):
    print(index, cities)

for index, element in enumerate(cities):
    print(index, cities)
