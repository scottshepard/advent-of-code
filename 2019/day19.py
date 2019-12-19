from copy import deepcopy
import numpy as np
from matplotlib import pyplot as plt
from utils import read_input
from intcode import IntcodeComputer

import pdb


input = read_input('day19.txt')[0]

class Scanner:

    def __init__(self, input):
        self.input = deepcopy(input)
        self.area = np.zeros((50, 50))


    def scan(self, shape):
        orig_shape = self.area.shape
        if shape[0] > self.area.shape[0]:
            # pdb.set_trace()
            self.area = np.append(self.area, np.zeros((shape[0]-self.area.shape[0], self.area.shape[1])), axis=0)
        elif shape[1] > self.area.shape[1]:
            self.area = np.append(self.area, np.zeros((self.area.shape[0], shape[1]-self.area.shape[1])), axis=1)
        for i in range(self.area.shape[0]):
            for j in range(self.area.shape[1]):
                IC = IntcodeComputer(self.input)
                val, _ = IC.next([i,j])
                self.area[i,j] = val[0]
        return self.area


s = Scanner(input)
a = s.scan((50,50))
plt.imshow(s.area, interpolation='nearest')
plt.savefig('day19_part1.png')
# print('Solution to Day 19 Part I is {}'.format(sum(sum(a))))



