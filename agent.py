from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
import numpy as np
from random import choice


class Agent:
    def __init__(self, game, player=1, learning_rate=0.001, epsilon=0.05):
        self.learning_rate = learning_rate
        self.model = self._build_model(game)
        self.player = player
        self.epsilon = epsilon
        self.score = 0
        self.memory_short = []
        self.memory_long = []

    def _build_model(self, game):
        board_size = game.BOARD_WIDTH * game.BOARD_HEIGHT
        model = Sequential()
        model.add(Dense(24, input_dim=board_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(game.BOARD_WIDTH, activation='softmax'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def eval_cell(self, cell):
        if cell == 0:
            return 0
        elif cell == self.player:
            return 1
        else:
            return -1

    def get_state(self, game):
        [self.eval_cell(cell) for cell in game.get_state]

    def act(self, game):
        state = game.get_state()
        act_values = self.model.predict(np.array([state]))
        action = np.argmax(act_values[0])
        if np.random.rand() <= self.epsilon:
            action = choice(range(game.BOARD_WIDTH))
        self.memory_short.append([state, act_values])
        return action, act_values

    def clear_short(self):
        self.memory_short = []

    def clear_long(self):
        self.memory_long = []

    def memorise(self, victory: bool):
        def review(x, v):
            if v:
                return x
            else:
                return 1 - x
        self.memory_long += [[state, review(x, victory)] for state, x in self.memory_short]
        self.clear_short()

    def train(self, epochs=10):
        states = np.array([x[0] for x in self.memory_long])
        actions = np.array([x[1][0] for x in self.memory_long])
        self.model.fit(states, actions, epochs=epochs)
        self.clear_long()

    def save(self, filename):
        self.model.save_weights(filename)

    def load(self, filename):
        self.model.load_weights(filename)
