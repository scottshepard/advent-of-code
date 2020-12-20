import re
import math
import numpy as np
from utils import read_input

def split(word):
    '''
    Split a string into a list of chars
    '''
    return [char for char in word]

class Tile:

    def __init__(self, id, body):
        self.id = id
        self.raw = body
        self.body = [split(line) for line in body]
        self.rotations = \
            [np.rot90(self.body, k=n) for n in range(4)] + \
            [np.rot90(np.fliplr(self.body), k=n) for n in range(4)]

def create_tiles(input):
    tiles = []
    for line in input:
        id = re.search('([0-9]+)', line[0]).group(0)
        tiles.append(Tile(id, line[1:]))
    return tiles




sample_input = [line.split('\n') for line in read_input('day20_test.txt', '\n\n')]
tiles = create_tiles(sample_input)
grid_size = int(math.sqrt(len(tiles)))
grid = [[None]*grid_size for i in range(grid_size)]
for i in range(grid_size):
    for j in range(grid_size):
        pass

