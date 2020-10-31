import copy
from itertools import zip_longest


def get_last_nonzero_index(lst):
    for element in reversed(lst):
        if element != 0:
            return lst.index(element)
    return 0


def val(x):
    if x is None:
        return 0
    else:
        return x


class Polynomial:

    def __init__(self, coefficients: list):
        coefficients = coefficients[:get_last_nonzero_index(coefficients) + 1]
        self.coefficients = coefficients

    def calculate(self, x: float):
        return sum([x ** i * self.coefficients[i] for i in range(len(self.coefficients))])

    def __str__(self):
        return ' + '.join([str(self.coefficients[i]) + '*x^' + str(i) for i in
                           range(len(self.coefficients)) if self.coefficients[i] != 0])

    def __bool__(self):
        if self.coefficients[-1] == 0:
            return False
        else:
            return True

    def __add__(self, other):
        if isinstance(other, (int, float, complex)):
            coefficients = copy.copy(self.coefficients)
            coefficients[0] += other
            return Polynomial(coefficients)
        else:
            coefficients = [val(a) + val(b) for a, b in zip_longest(self.coefficients, other.coefficients)]
            return Polynomial(coefficients)

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        if isinstance(other, (int, float, complex)):
            coefficients = copy.copy(self.coefficients)
            coefficients[0] -= other
            return Polynomial(coefficients)
        else:
            coefficients = [val(a) - val(b) for a, b in zip_longest(self.coefficients, other.coefficients)]
            return Polynomial(coefficients)

    def __isub__(self, other):
        self = self - other
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            coefficients = [other * c for c in self.coefficients]
            coefficients = coefficients[:get_last_nonzero_index(coefficients) + 1]
            return Polynomial(coefficients)
        else:
            result = Polynomial([0])
            for i in range(len(other.coefficients)):
                result += Polynomial([0] * i + [other.coefficients[i] * c for c in self.coefficients])
            return result

    def __imul__(self, other):
        self = self * other
        return self


if __name__ == "__main__":
    p1 = Polynomial([1, 0, 2])
    p2 = Polynomial([3, 3, 3, 1, 0])
    print(p1)
    print(p1 + p2)
    print(p1 + 2)
    print(p2 - p1)
    print(p1.calculate(2))
    print(p1 * p2)
