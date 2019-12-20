from copy import deepcopy
import numpy as np
from matplotlib import pyplot as plt
from utils import read_input
from intcode import IntcodeComputer

import pdb


input = read_input('day19.txt')[0]

class Scanner:

    def __init__(self, input, base_shape = (50,50)):
        self.input = deepcopy(input)
        self.area = np.zeros(base_shape)
        self.scan(0, base_shape[0], 0, base_shape[1])

    def expand(self, new_shape):
        if new_shape[0] > self.area.shape[0]:
            self.expand_rows(new_shape[0] - self.area.shape[0])
        if new_shape[1] > self.area.shape[1]:
            self.expand_cols(new_shape[1] - self.area.shape[1])

    def expand_rows(self, n_rows):
        new_rows = np.zeros((n_rows, self.area.shape[1]))
        self.area = np.append(self.area, new_rows, axis=0)

    def expand_cols(self, n_cols):
        new_cols = np.zeros((self.area.shape[0], n_cols))
        self.area = np.append(self.area, new_cols, axis=1)

    def explore(self, new_shape):
        orig_shape = self.area.shape
        self.expand(new_shape)
        self.scan(orig_shape[0], new_shape[0], 0, orig_shape[1])
        self.scan(0, orig_shape[0], orig_shape[1], new_shape[1])

    def scan(self, x1, x2, y1, y2):
        for i in range(x1, x2):
            for j in range(y1, y2):
                IC = IntcodeComputer(self.input)
                val, _ = IC.next([i,j])
                self.area[i,j] = val[0]

    def find_box(self, size):
        for i in

    def box_fit(self, x, y, size):
        if (x + size) >= self.area.shape[0] or (y + size) >= self.area.shape[1]:
            return False
        else:
            return (self.area[x,y] + self.area[x+size, y] + self.area[x, y+size] + self.area[x+size, y+size]) == 4


s = Scanner(input, (50,50))
plt.imshow(s.area, interpolation='nearest')
plt.savefig('day19_part1.png')
print('Solution to Day 19 Part I is {}'.format(sum(sum(s.area))))



