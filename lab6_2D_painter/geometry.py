class Vector2D:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self = self + other # wektor jest modyfikowalny, czy niemodyfikowalny?
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self = self - other
        return self


def check_numeric(size):    # myląca nazwa
    for i, v in enumerate(size):
        size[i] = float(v)
    return size


class Shape:
    COLORS = {'black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow'}

    def __init__(self, *size):
        self.size = check_numeric(list(size))
        self.center = Vector2D(0, 0)
        self.border_color = 'white'
        self.background_color = 'white'

    def __str__(self):
        return 'center: {}, size: {}, border color: {}, background color: {}'.format(self.center, self.size,
                                                                                     self.border_color,
                                                                                     self.background_color)

    def move(self, x, y):
        self.center += Vector2D(x, y)

    def scale(self, ratio):
        ratio = float(ratio)    # lepiej założyć, że już Pan dostał właściwy typ
        if ratio == 0:
            raise ValueError('Ratio must be non-zero!')
        self.size *= ratio

    def rotate(self, angle):
        pass

    def set_border_color(self, color):
        if color in Shape.COLORS:
            self.border_color = color
        else:
            raise ValueError('Unknown color!')

    def set_background_color(self, color):
        if color in Shape.COLORS:
            self.background_color = color
        else:
            raise ValueError('Unknown color!')


class Circle(Shape):
    def __init__(self, *size):
        if len(size) != 1:
            raise ValueError('Wrong size format')
        super().__init__(*size)

    def __str__(self):
        return 'Circle (' + super().__str__() + ')'


class Polygon(Shape):

    def __init__(self, *size):
        super().__init__(*size)
        self.angle = 0

    def rotate(self, angle):
        self.angle = 360 % (self.angle + int(angle))

    def __str__(self):
        return super().__str__()[:-1] + ', rotation: {})'.format(self.angle)


class Square(Polygon):

    def __init__(self, *size):
        if len(size) != 1:
            raise ValueError('Wrong size format')
        super().__init__(*size)

    def __str__(self):
        return 'Square (' + super().__str__() + ')'


class Rectangle(Polygon):

    def __init__(self, *size):
        if len(size) != 2:
            raise ValueError('Wrong size format')
        super().__init__(*size)

    def __str__(self):
        return 'Rectangle (' + super().__str__() + ')'


class Triangle(Polygon):

    def __init__(self, *size):
        if len(size) != 3:
            raise ValueError('Wrong size format')
        super().__init__(*size)
        if 2*max(self.size) >= sum(self.size):
            raise ValueError('Triangle inequality unsatisfied!')

    def __str__(self):
        return 'Triangle (' + super().__str__() + ')'
