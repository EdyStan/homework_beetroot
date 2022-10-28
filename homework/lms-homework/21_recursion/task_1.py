def to_power(x, exp: int):
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")

    elif exp == 0:
        return 1

    else:
        return to_power(x, exp - 1) * x


assert to_power(2, 3) == 8
assert to_power(3.5, 2) == 12.25
