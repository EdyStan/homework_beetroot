"""
Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total
price of stock.
"""

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
price = 0

for fruit in stock:
    price += stock[fruit] * prices[fruit]

print(str(int(price)) + " bucks")
