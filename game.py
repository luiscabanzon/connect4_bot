import sys
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


def print_board():
    for column in board:
        print(' '.join([str(c) for c in column]))

players = [0,1]
turn = 0

while True:
    player = turn % 2
    action = int(input("Choose column : "))
    play_turn(action, player)
    print_board()
    if check_end():
        break
    turn += 1

