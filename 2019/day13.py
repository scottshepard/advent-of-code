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

    def __init__(self, input, q=None):
        self.input_raw = deepcopy(input)
        self.IC = IntcodeComputer(input)
        if q is not None:
            self.IC.source_code[0] = q
        self.screen = np.ndarray((24, 42), dtype=np.dtype('b'))
        self.next_screen(0)
        self.score = 0

    def play(self):
        while not self.game_over:
            self.next()

    def next(self):
        i = self.next_input()
        self.next_screen(i)

    def next_screen(self, i):
        self.IC.halt = False
        _, self.game_over = self.IC.next([i])
        n_squares = int(len(self.IC.outputs) / 3)
        squares = np.reshape(self.IC.outputs, (n_squares, 3))
        for square in squares:
            x, y, c = tuple(square)
            if x==-1 and y==0:
                self.score = c
            else:
                if c == 3:
                    self.x_paddle = x
                elif c == 4:
                    self.x_ball = x
                self.screen[y][x] = c

    def next_input(self):
        if self.x_paddle > self.x_ball:
            return -1
        elif self.x_paddle < self.x_ball:
            return 1
        else:
            return 0

    def __repr__(self):
        out = ''
        for line in self.screen:
            out += ''.join([self.square_char(n) for n in line]) + '\n'
        return out

    def square_char(self, n):
        return Breakout.square_chars[n]



input = read_input('day13.txt')[0]

breakout = Breakout(input)
print('Solution to Day 13 part I is {}'.format((breakout.screen == 2).sum()))

breakout = Breakout(input, 2)
breakout.play()
print('Solution to Day 13 part II is {}'.format(breakout.score))
