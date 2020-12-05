def quadratic_equation(a, b, c):
    if a == b == c == 0:
        raise ValueError('At least one of coefficients must be non-zero!')  # komunikat nieprawdziwy
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return {}
    elif delta == 0:
        return {-b/(2*a)}   # ZeroDivisionError
    else:
        return {(-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a)}


def find_straight_line(point1, point2):
    if point1[0] == point2[0] and point1[1] == point2[1]:   # <=> point1 == point2
        raise ValueError('Provided points are equal!')
    return (point1[1] - point2[1]) / (point1[0] - point2[0]),\
        point1[1] - point1[0]*(point1[1] - point2[1]) / (point1[0] - point2[0]) # ZeroDivisionError
