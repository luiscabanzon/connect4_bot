import sys
import numpy as np

print(sys.version)

BOARD_WIDTH = 7
BOARD_HEIGHT = 6

board = [[] for column in range(BOARD_WIDTH)]


def play_turn(column, player):
    global board
    board[column].append(player)


def check_end():
    for column in board:
        if len(column) >= BOARD_HEIGHT:
            return True
    return False


def check_victory(space, player):
    # Space: 2-D array (not matrix!)
    pattern = str(player) * 4
    diagonals = np.max([BOARD_HEIGHT, BOARD_WIDTH])
    space = [np.pad(s, pad_width=(0, diagonals - len(s)), mode='constant', constant_values=3) for s in space]
    space = np.matrix(space, dtype=np.int32)
    space_flip = np.fliplr(space)
    print(space)
    for i in range(diagonals * -1, diagonals):
        if pattern in "".join([str(s) for s in space.diagonal(i).tolist()[0]]) \
                or pattern in "".join([str(s) for s in space_flip.diagonal(i).tolist()[0]]):
            return True
    for row in space.tolist():
        if pattern in "".join([str(r) for r in row]):
            return True
    for column in space.T.tolist():
        if pattern in "".join([str(c) for c in column]):
            return True
    return False


def print_board():
    for column in board:
        print(' '.join([str(c) for c in column]))

players = [0, 1]
turn = 0

while True:
    player = turn % 2
    action = int(input("Choose column : "))
    play_turn(action, player)
    print_board()
    if check_victory(board, player):
        print("Player %s WINS!" % player)
        break
    if check_end():
        break
    turn += 1
