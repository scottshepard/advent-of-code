import copy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from utils import read_input


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

    def decode_pixel(self, w, h):
        out = None
        for layer in self.layers:
            pixel = layer[h][w]
            if pixel == '2':
                pass
            elif pixel == '1' and out is None:
                out = 1
            elif pixel == '0' and out is None:
                out = 0
        return out

    def decode_image(self):
        image = np.empty([self.width, self.height], dtype=int)
        for w in range(0, self.width):
            for h in range(0, self.height):
                image[w, h] = self.decode_pixel(w, h)

        return image


if __name__ == '__main__':
    test_input = read_input('day08_test.txt')
    t1_sid = SpaceImageDecoder(test_input[0], 3, 2)
    t2_sid = SpaceImageDecoder(test_input[1], 2, 2)

    input = read_input('day08.txt')[0]
    sid = SpaceImageDecoder(input, 25, 6)
    print('Solution to part 1 is {}'.format(sid.solve1()))

    img = sid.decode_image()
    plt.imshow(img, interpolation='nearest')
    plt.savefig('day08_part2.png')
    print('Solution to part 2 is saved as an image to day08_part2.png')
