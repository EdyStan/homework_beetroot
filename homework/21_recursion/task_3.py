def mult(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    if a < 0 or b < 0:
        raise ValueError("This function works only with positive integers")

    return mult(a, b - 1) + a


assert mult(2, 4) == 8
assert mult(2, 0) == 0
assert mult(0, 6) == 0
assert mult(3, 33) == 99
