from re import findall


class FractionClass:
    def __init__(self, fraction_string):
        t = [int(s) for s in findall(r'\b\d+\b', fraction_string)]
        self.numerator = t[0]
        self.denominator = t[1]
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
