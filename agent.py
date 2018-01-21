from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam


class Agent:
    def __init__(self, game, learning_rate=0.001):
        self.learning_rate = learning_rate
        self.model = self._build_model(game)

    def _build_model(self, game):
        board_size = game.BOARD_WIDTH * game.BOARD_HEIGHT
        model = Sequential()
        model.add(Dense(24, input_dim=board_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(game.BOARD_WIDTH, activation='softmax'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model
