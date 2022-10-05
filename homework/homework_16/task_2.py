# how do I make it work with default values?

# def my_range(end, start=0, step=1):
#     start, end = end, start
#     if end < start and step > 0 or end > start and step < 0:
#         raise StopIteration
#     while start != end:


def my_range(start, end, step=1):
    while True:
        if start >= end and step > 0 or start <= end and step < 0:
            break
        yield start
        start += step


list_1 = [i for i in range(9, 1, -1)]
list_2 = [i for i in my_range(9, 1, -1)]

assert list_2 == list_1

list_3 = [i for i in range(1, 90, 4)]
list_4 = [i for i in my_range(1, 90, 4)]

assert list_3 == list_4

list_5 = [i for i in range(5, 5, 4)]
list_6 = [i for i in my_range(5, 5, 4)]

assert list_5 == list_6
