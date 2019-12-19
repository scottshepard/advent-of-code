from copy import deepcopy
import numpy as np
from utils import read_input
from intcode import IntcodeComputer


class Breakout:

    square_chars = {
        0: ' ',
        1: '#',
        2: 'X',
        3: '-',
        4: 'o'
    }

    def __init__(self, input):
        self.input_raw = deepcopy(input)
        self.IC = IntcodeComputer(input)
        self.screen = np.ndarray((24, 42), dtype=np.dtype('b'))

    def next(self, i):
        self.IC.halt = False
        self.IC.next([i])
        n_squares = int(len(self.IC.outputs) / 3)
        squares = np.reshape(self.IC.outputs, (n_squares, 3))
        for square in squares:
            x, y, c = tuple(square)
            if x==-1 and y==0:
                self.score = c
            else:
                self.screen[y][x] = c

    def __repr__(self):
        out = ''
        for line in self.screen:
            out += ''.join([self.square_char(n) for n in line]) + '\n'
        return out

    def square_char(self, n):
        return Breakout.square_chars[n]





input = read_input('day13.txt')[0]

#breakout = Breakout(input)
#breakout.next(0)
#print('Solution to Day 13 part I is {}'.format((breakout.screen == 2).sum()))

breakout = Breakout(input)
breakout.IC.source_code[0] = 2
breakout.next(0)
print(breakout)



