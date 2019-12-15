import numpy as np
import pandas as pd
from utils import read_input


class Wire:

    def __init__(self, input):
        self.directions = input.split(',')
        self.coords = {}
        self.moves = 0
        self.map_path()

    def map_path(self):
        x, y = 0, 0
        for dir in self.directions:
            if dir[0] == 'R':
                mag = int(dir[1:])
                for i in range(mag):
                    x += 1
                    self.moves += 1
                    self.coords[(x, y)] = self.moves
            elif dir[0] == 'L':
                mag = int(dir[1:])
                for i in range(mag):
                    x -= 1
                    self.moves += 1
                    self.coords[(x, y)] = self.moves
            elif dir[0] == 'U':
                mag = int(dir[1:])
                for i in range(mag):
                    y += 1
                    self.moves += 1
                    self.coords[(x, y)] = self.moves
            elif dir[0] == 'D':
                mag = int(dir[1:])
                for i in range(mag):
                    y -= 1
                    self.moves += 1
                    self.coords[(x, y)] = self.moves


def find_intersections(wire1, wire2):
    return set(wire1.coords.keys()).intersection(set(wire2.coords.keys()))



def manhattan_distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def solve1(input1, input2):
    w1 = Wire(input1)
    w2 = Wire(input2)
    intersections = find_intersections(w1, w2)
    distances = []
    for intsec in intersections:
        distances.append(manhattan_distance(intsec, [0,0]))
    return np.array(distances).min()


def solve2(input1, input2):
    w1 = Wire(input1)
    w2 = Wire(input2)
    intersections = find_intersections(w1, w2)
    steps = []
    for intersection in intersections:
        steps.append(w1.coords[intersection] + w2.coords[intersection])
    return pd.Series(steps).min()

if __name__ == '__main__':
    test_inputs = read_input('day03_test.txt')
    assert solve1(test_inputs[0], test_inputs[1]) == 6
    assert solve1(test_inputs[3], test_inputs[4]) == 159
    assert solve1(test_inputs[6], test_inputs[7]) == 135

    input = read_input('day03.txt')
    print('Solution to part 1 is {}'.format(solve1(input[0], input[1])))
    print('Solution to part 2 is {}'.format(solve2(input[0], input[1])))


