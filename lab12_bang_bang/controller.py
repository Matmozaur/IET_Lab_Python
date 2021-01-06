from board import Board
from player import Player


def run_single_match(width, player1, player2, inplace):
    board = Board(width, player1, player2)
    current = player1
    result = None
    while result is None:
        try:
            angle, velocity = current.get_move()
        except ValueError:
            print('Wrong input!')
            continue
        result = board.shoot(current, angle, velocity)
        board.visualise(inplace)
        current = player2 if current == player1 else player1
    return result


def run_game(points_to_win=2, width=1000, inplace=False):
    player1 = Player('first')
    player2 = Player('second')
    while True:
        winner = run_single_match(width, player1, player2, inplace)
        print(winner.name + ' won match!')
        winner.points += 1
        if winner.points >= points_to_win:
            print(winner.name + ' won game!')
            return winner
