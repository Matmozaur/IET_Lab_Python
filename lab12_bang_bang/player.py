class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.x = 0
        self.y = 0

    def put_on_board(self, x, y):
        self.x = x
        self.y = y

    def get_move(self):
        a, v = [float(x) for x in input('{} - please provide angle and velocity'.format(self.name)).split()]
        return a, v
