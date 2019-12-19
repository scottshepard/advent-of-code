from copy import deepcopy
import numpy as np
from utils import read_input
from intcode import IntcodeComputer


class Breakout:

    def __init__(self, input):
        self.input_raw = deepcopy(input)
        self.IC = IntcodeComputer(input)
        self.screen = np.ndarray((24, 42), dtype=np.dtype('b'))

    def next(self):
        self.IC.next()
        n_squares = int(len(self.IC.outputs) / 3)
        squares = np.reshape(self.IC.outputs, (n_squares, 3))
        for square in squares:
            x, y, c = tuple(square)
            self.screen[y][x] = c




input = read_input('day13.txt')[0]

breakout = Breakout(input)
breakout.next()

print('Solution to Day 13 part I is {}'.format((breakout.screen == 2).sum()))



