import unittest

from lab7_unit_tests.main.math_utils import quadratic_equation, find_straight_line

# trochę ubogie te testy
class QuadraticEquationTest(unittest.TestCase):
    # Z tego co widziałem przeglądając pobieżnie internet niestety niemożliwe jest w tym momencie używanie
    # almostEqual na setach przy użyciu wyłaćznie biblioteki unittest, dlatego tutaj robię ta kombinację z
    # zaokrąglaniem.
    def test_wrong_input(self):
        self.assertRaises(ValueError, quadratic_equation, 0, 0, 0)

    def test_delta_zero(self):
        result = set(map(lambda x: round(x, 5), quadratic_equation(2, 4, 2)))
        self.assertCountEqual({-1}, result)

    def test_delta_negative(self):
        self.assertCountEqual({}, quadratic_equation(2, 1, 3))

    def test_delta_positive(self):
        result1 = set(map(lambda x: round(x, 5), quadratic_equation(1, 0, -1)))
        self.assertCountEqual({1, -1}, result1)
        result2 = set(map(lambda x: round(x, 5), quadratic_equation(3, 3, -18)))
        self.assertCountEqual({2, -3}, result2)


class FindStraightLineTest(unittest.TestCase):
    def test_wrong_input(self):
        self.assertRaises(ValueError, find_straight_line, (1, 2), (1, 2))

    def test_good_input(self):
        result1 = list(map(lambda x: round(x, 5), find_straight_line((0, 0), (1, 1))))
        self.assertEqual([1, 0], result1)
        result2 = list(map(lambda x: round(x, 5), find_straight_line((-10, 10), (10, 0))))
        self.assertEqual([-0.5, 5], result2)


if __name__ == "__main__":
    unittest.main()

