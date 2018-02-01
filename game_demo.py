from random import choice  # For demo purposes
from game import Game

# Demo below (with random moves)
players = [1, 2]
turn = 0
g = Game()
while not g.check_victory(players[turn % 2]):
    player = players[turn % 2]
    c = choice(range(7))
    g.play_turn(c, player)
    if g.check_end():
        break
    print(g.get_state())
    turn += 1
