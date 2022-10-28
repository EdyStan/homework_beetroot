def sum_digits(num: int) -> int:
    # base case when your "positive" integer get to 0
    if num == 0:
        return 0
    # base case when your "negative" integer get is between -10 and 0
    if -10 < num < 0:
        return num
    # recursion for positive integer
    elif num > 0:
        return (num % 10) + sum_digits(num // 10)
    # recursion for negative integer
    elif num < 0:
        return -(abs(num) % 10) + sum_digits(-(abs(num) // 10))


print(sum_digits(12345))
print(sum_digits(-123))
