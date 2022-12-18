
def function_one(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item2)


# ------------------------------------------------------------


steps = []


def function_two(n):
    return n


for i in range(1, 100):
    steps.append(function_two(i))


# ------------------------------------------------------------


def function_three(items):
    result = items[0] * items[0]
    print(result)
