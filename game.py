import sys
import numpy as np
import itertools
from random import choice  # For demo purposes

print(sys.version)


class Game:
    def __init__(self, BOARD_WIDTH=7, BOARD_HEIGHT=6):
        self.BOARD_WIDTH = BOARD_WIDTH
        self.BOARD_HEIGHT = BOARD_HEIGHT
        self.board = [[] for column in range(BOARD_WIDTH)]

    def play_turn(self, column, player):
        self.board[column].append(player)

    def check_end(self):
        for column in self.board:
            if len(column) >= self.BOARD_HEIGHT:
                return True
        return False

    def check_victory(self, player):
        pattern = str(player) * 4
        diagonals = np.max([self.BOARD_HEIGHT, self.BOARD_WIDTH])
        space = [np.pad(s, pad_width=(0, diagonals - len(s)), mode='constant', constant_values=1) for s in self.board]
        space = np.matrix(space, dtype=np.int32)
        space_flip = np.fliplr(space)
        print(space)
        for i in range(diagonals * -1, diagonals):
            if pattern in "".join([str(s) for s in space.diagonal(i).tolist()[0]]) \
                    or pattern in "".join([str(s) for s in space_flip.diagonal(i).tolist()[0]]):
                print("Player %s WINS!" % player)
                return True
        for row in space.tolist():
            if pattern in "".join([str(r) for r in row]):
                print("Player %s WINS!" % player)
                return True
        for column in space.T.tolist():
            if pattern in "".join([str(c) for c in column]):
                print("Player %s WINS!" % player)
                return True
        return False

    def get_board(self):
        return [np.pad(b, pad_width=(0, self.BOARD_HEIGHT - len(b)),
                       mode='constant', constant_values=0) for b in self.board]

    def get_input(self):
        return list(itertools.chain(*self.get_board()))


# Demo below (with random moves)
players = [0, 2]
turn = 0
g = Game()
while not g.check_victory(players[turn % 2]):
    player = players[turn % 2]
    c = choice(range(7))
    g.play_turn(c, player)
    if g.check_end():
        break
    print(g.get_input())
    turn += 1
