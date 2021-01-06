import math

import numpy as np
import matplotlib.pyplot as plt

from config import *
from player import Player


def choose_step(last):
    if last == 0:
        return np.random.choice([-2, -1, 0, 1, 2], p=[0.001, 0.004, 0.99, 0.004, 0.001])
    elif abs(last) == 1:
        return np.random.choice([i * np.sign(last) for i in range(3)], p=[0.01, 0.98, 0.01])
    elif abs(last) == 2:
        return np.random.choice([i * np.sign(last) for i in range(3)], p=[0.01, 0.09, 0.9])


def generate_area(width):
    roll = int(width / 10)
    width += roll - 1
    area = [np.random.uniform(0, width)]
    last = 0
    limit = width - 1
    i = 0
    while i < limit:
        last = choose_step(last)
        area.append(area[i - 1] + STEP * width * last)
        i += 1
    area = np.convolve(area, np.ones(roll) / roll, mode='valid')
    return area


def trajectory_generator(h, v, alpha):
    alpha = math.radians(alpha)
    x = 1
    while True:
        yield h + x * math.tan(alpha) - x ** 2 * G / (2 * v ** 2 * math.cos(alpha) ** 2)
        x += 1


class Board:

    def __init__(self, width, p1, p2):
        self.area = generate_area(width)
        self.width = width
        x1 = int(width * FIRST_X)
        x2 = int(width * SECOND_X)
        p1.put_on_board(x1, self.area[x1])
        self.player1 = p1
        p2.put_on_board(x2, self.area[x2])
        self.player2 = p2

    def shoot(self, player, angle, velocity):
        if angle == 90:
            return self.hit(player.x)
        dx = 1
        if player == self.player2:
            dx = -dx
        if angle > 90:
            angle = 180 - angle
            dx = -dx
        x0 = player.x
        for h in trajectory_generator(player.y, velocity, angle):
            x0 += dx
            if x0 >= self.width:
                return None
            elif h < self.area[x0]:
                return self.hit(x0)

    def visualise(self, inplace=False, path='temp'):
        """
        For exploratory testing only.
        """
        plt.figure(figsize=(15, 5))
        plt.plot(self.area, 'g')
        plt.plot(self.player1.x, self.player1.y, 'bo', markersize=15)
        plt.plot(self.player2.x, self.player2.y, 'ro', markersize=15)
        plt.fill_between(np.arange(self.width), min(self.area) - 10, self.area, color='g')
        axes = plt.gca()
        axes.set_ylim([min(self.area) - 2, 1.5 * max(self.area)])
        if inplace:
            plt.show()
        else:
            plt.interactive(False)
            plt.savefig(path)

    def hit(self, x0):
        winner = None
        if math.sqrt((self.player1.x - x0)**2 + (self.player1.y - self.area[x0])**2) <= R:
            winner = self.player2
        elif math.sqrt((self.player2.x - x0)**2 + (self.player2.y - self.area[x0])**2) <= R:
            winner = self.player1
        h0 = self.area[x0]
        for i in range(2*R+1):
            if self.area[x0-R+i] > (h0 - math.sqrt((2*R-i)*i)):
                self.area[x0-R+i] = (h0 - math.sqrt((2*R-i)*i))
        return winner


if __name__ == '__main__':
    player1 = Player('first')
    player2 = Player('second')
    board = Board(1000, player1, player2)
    board.visualise(path="temp_map_before.png")
    board.shoot(player1, 30, 50)
    board.shoot(player1, 60, 80)
    board.shoot(player1, 45, 50)
    board.visualise(path="temp_map_after.png")

