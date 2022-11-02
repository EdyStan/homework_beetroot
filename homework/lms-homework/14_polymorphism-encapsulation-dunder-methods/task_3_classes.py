from math import lcm, gcd
from re import findall


class FractionClass:
    def __init__(self, fraction_string):
        t = fraction_string.split('/')
        self.numerator = int(t[0])
        self.denominator = int(t[1])
        if self.denominator == 0:
            raise ZeroDivisionError('Denominator can\'t take the value of 0')
        self.float_fraction = self.numerator / self.denominator

    def __lt__(self, other):
        return self.float_fraction < other.float_fraction

    def __le__(self, other):
        return self.float_fraction <= other.float_fraction

    def __gt__(self, other):
        return self.float_fraction > other.float_fraction

    def __ge__(self, other):
        return self.float_fraction >= other.float_fraction

    def __eq__(self, other):
        return self.float_fraction == other.float_fraction

    def __ne__(self, other):
        return self.float_fraction != other.float_fraction

    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, other):
        common_denominator = lcm(self.denominator, other.denominator)
        numerator_1 = int(self.numerator * (common_denominator / self.denominator))
        numerator_2 = int(other.numerator * (common_denominator / other.denominator))
        divisor = gcd(numerator_1 + numerator_2, common_denominator)
        return str(int((numerator_1 + numerator_2) / divisor)) + '/' + str(int(common_denominator / divisor))

    def __sub__(self, other):
        common_denominator = lcm(self.denominator, other.denominator)
        numerator_1 = int(self.numerator * (common_denominator / self.denominator))
        numerator_2 = int(other.numerator * (common_denominator / other.denominator))
        divisor = gcd(numerator_1 - numerator_2, common_denominator)
        return str(int((numerator_1 - numerator_2) / divisor)) + '/' + str(int(common_denominator / divisor))

    def __mul__(self, other):
        common_numerator = self.numerator * other.numerator
        common_denominator = self.denominator * other.denominator
        divisor = gcd(common_denominator, common_numerator)
        return str(int(common_numerator / divisor)) + '/' + str(int(common_denominator / divisor))

    def __truediv__(self, other):
        common_numerator = self.numerator * other.denominator
        common_denominator = self.denominator * other.numerator
        divisor = gcd(common_denominator, common_numerator)
        return str(int(common_numerator / divisor)) + '/' + str(int(common_denominator / divisor))
