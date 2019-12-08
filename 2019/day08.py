import advent_of_code as aoc
import copy
import numpy as np
import pandas as pd
import pdb

class SpaceImageDecoder:

    def __init__(self, input, width, height):
        self.input_raw = copy.deepcopy(input)
        self.input = copy.deepcopy(input)
        self.width = width
        self.height = height
        self.layers = self.make_layers()

    def make_layers(self):
        i = 0
        layers = []
        while i < len(self.input):
            end_i = i + self.width * self.height
            pixels = self.input[i:end_i]
            j = 0
            layer = []
            while j < len(pixels):
                end_j = j + self.width
                line = pixels[j:end_j]
                layer.append(line)
                j = end_j
            i = end_i
            layers.append(layer)
        return layers

    def count_chars_in_layer(self, layer, char='0'):
        return pd.Series([l.count(char) for l in layer]).sum()

    def solve1(self):
        zeros = pd.Series([self.count_chars_in_layer(l) for l in self.layers])
        i = zeros[zeros == zeros.min()].index[0]
        return self.count_chars_in_layer(self.layers[i], '1') * self.count_chars_in_layer(self.layers[i], '2')


if __name__ == '__main__':
    test_input = aoc.read_input('day08_test.txt')[0]
    sid = SpaceImageDecoder(test_input, 3, 2)

    input = aoc.read_input('day08.txt')[0]
    sid = SpaceImageDecoder(input, 25, 6)
    print('Solution to part 1 is {}'.format(sid.solve1()))
