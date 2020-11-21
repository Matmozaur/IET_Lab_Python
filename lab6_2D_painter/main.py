from lab6_2D_painter.geometry import *


def check_name(name):
    if name[0].isdigit():
        ValueError('Name cannot start with a digit!')
    for s in name:
        if not s.isalnum() and s != '_':
            raise ValueError('Name cannot contain!')
    return name


class Board:
    FIGURES = {'circle': Circle, 'rectangle': Rectangle, 'triangle': Triangle, 'square': Square}

    def __init__(self):
        self.figures = dict()

    def add(self, figure, name, size):
        name = check_name(name)
        if name in self.figures.keys():
            raise ValueError('Name is not unique!')
        else:
            self.figures[name] = Board.FIGURES[figure.lower()](size)

    def remove(self, name):
        if name in self.figures.keys():
            del self.figures[name]
        else:
            raise ValueError('Unknown name!')

    def help(self):
        print('add <figure> <name> <size>\n\
        remove <name>\n\
        move <name> <vector>\n\
        scale <name> <ratio>\n\
        rotate <name> <angle>\n\
        set border color <name> <color>\n\
        set background color <name> <color>\n\
        help\n\
        quit\n\
        <figure> to jedno z: circle, square, rectangle, triangle\n\
        <name> - dowolny unikatowy identyfikator mogący zawierać litery, cyfry i podkreślniki, nie zaczynający się od \
         cyfry\n\
        <ratio> - dowolna liczba rzeczywista, różna od 0\n\
        <angle> - dowolny kąt w stopniach\n\
        <color> to jedno z: black, white, red, green, blue, cyan, magenta, yellow\n\
        Każda figura po dodaniu ma środek w punkcie (0, 0).')

    def quit(self):
        for f in self.figures.values():
            print(f)

    BOARD_COMMANDS = {'help': help, 'quit': quit, 'add': add, 'remove': remove}
    FIGURE_COMMANDS = {'move', 'scale', 'rotate', 'set_border_color', 'set_background_color'}

    class Line:

        def __init__(self, line):
            parts = line.split()
            self.command = parts[0].lower()
            if self.command in Board.FIGURE_COMMANDS:
                self.name = parts[1]
                self.params = parts[2:]
            else:
                self.params = parts[1:]

    def run(self):
        while 1:
            try:
                line = self.Line(input('Type command: '))
                if line.command in self.BOARD_COMMANDS:
                    self.BOARD_COMMANDS[line.command](self, *line.params)
                if line.command in self.FIGURE_COMMANDS:
                    self.execute(line.command, line.name, line.params)
                if line.command == 'quit':
                    break
            except (ValueError, IndexError, TypeError) as e:
                print(e)

    def execute(self, method, name, params):
        if name in self.figures.keys():
            if method == 'move':
                self.figures[name].move(*params)
            if method == 'scale':
                self.figures[name].scale(*params)
            if method == 'rotate':
                self.figures[name].rotate(*params)
            if method == 'set_border_color':
                self.figures[name].set_border_color(*params)
            if method == 'set_background_color':
                self.figures[name].set_background_color(*params)
        else:
            raise ValueError('Unknown name!')


if __name__ == '__main__':
    board = Board()
    board.run()
