import copy
from itertools import zip_longest

"""
    Czy defaultdict jest dobrym pomysłem na przechowywanie współczynników? - tak, myślę że sprawdził by się całkiem 
    dobrze, można w nim zdefiniować domyślną wartośc na 0, więc nie trzeba byłoby się aż tyle martwić o to ograniczenie.

    Czy taki wielomian zadziałałby w dziedzinie macierzy lub liczb zespolonych? - w dziedzinie zespolonych, jeśli nie ma
     błędów w implementacji to powinien działać zarówno jeśli chodzi o zespolone wartości jak i współczynniki, jeśli
     chodzi o macierze to na pewno nie zadziała na wszystkich (tzn.minimalnym wymaganiem jest to żeby były kwadratowe,
     oraz jeśli chcemy uzywać mnożenia, były tych samych rozmiarów). Oprócz tego oczywiście ich implementacja musi być
     kompatybilna z poniższym kodem, czyli muszą być w niej zaimplementowane przeciążenia odpowiednich operatorów.
     Jeśli ponadto macierze miałyby być współczynnikami to wartościami również musiałyby być wyłącznie macierze
     kwadratowe określonych rozmiarów
"""


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

    def set_coefficient(self, position, c):
        degree = len(self.coefficients)
        if position < degree:
            self.coefficients[position] = c
        else:
            self.coefficients += [0] * (position - degree)
            self.coefficients.append(c)

    # def __setitem__(self, key, value):
    #     for syntax: P[1] = x ...
    #
    # def __getitem__(self, item):
    #     for syntax: x = P[1] ...
    #
    # def __setattr__(self, key, value):
    #     for syntax: P.a1 = x ...
    #
    # def __getattr__(self, item):
    #     for syntax: x = P.a1 ...

    def __call__(self, x: float):
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

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Polynomial([other]) - self

    def __rmul__(self, other):
        return self * other


if __name__ == "__main__":
    p1 = Polynomial([1])
    p2 = Polynomial([3, 3, 3, 1, 0])
    p1.set_coefficient(2, 2)
    print(p1)
    print(p1 + p2)
    print(p1 + 2)
    print(p2 - p1)
    print(p1(2))
    print(p1(2j))
    print(p1 * p2)

    p1 = Polynomial([0, 2j])
    p2 = Polynomial([3, 3 + 3j, 1])
    print(p1)
    print(p1 + p2)
    print(p1 + 2)
    print(p2 - p1)
    print(p1(2))
    print(p1(2+1j))
    print(p1 * p2)
