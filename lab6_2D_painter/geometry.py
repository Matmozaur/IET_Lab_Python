class Vector2D:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self = self - other
        return self


class Shape:
    COLORS = {'black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow'}

    def __init__(self, size):
        self.size = float(size)
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
        ratio = float(ratio)
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

    def __str__(self):
        return 'Circle (' + super().__str__() + ')'


class Polygon(Shape):

    def __init__(self, size):
        super().__init__(size)
        self.angle = 0

    def rotate(self, angle):
        self.angle = 360 % (self.angle + int(angle))

    def __str__(self):
        return super().__str__()[:-1] + ', rotation: {})'.format(self.angle)


class Square(Shape):

    def __str__(self):
        return 'Square (' + super().__str__() + ')'


class Rectangle(Shape):

    def __str__(self):
        return 'Rectangle (' + super().__str__() + ')'


class Triangle(Shape):

    def __str__(self):
        return 'Triangle (' + super().__str__() + ')'
