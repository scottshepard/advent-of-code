import advent_of_code as aoc
import numpy as np
import pdb


class Wire:

    def __init__(self, input):
        self.directions = input.split(',')
        self.coords = set()
        self.map_path()

    def map_path(self):
        x, y = 0, 0
        for dir in self.directions:
            if dir[0] == 'R':
                mag = int(dir[1:])
                for i in range(mag):
                    x += 1
                    self.coords.add((x, y))
            elif dir[0] == 'L':
                mag = int(dir[1:])
                for i in range(mag):
                    x -= 1
                    self.coords.add((x, y))
            elif dir[0] == 'U':
                mag = int(dir[1:])
                for i in range(mag):
                    y += 1
                    self.coords.add((x, y))
            elif dir[0] == 'D':
                mag = int(dir[1:])
                for i in range(mag):
                    y -= 1
                    self.coords.add((x, y))


def find_intersections(wire1, wire2):
    return set(wire1.coords).intersection(set(wire2.coords))



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



if __name__ == '__main__':
    test_inputs = aoc.read_input('day03_test.txt')
    print('Solution to test input 1 is {}'.format(solve1(test_inputs[0], test_inputs[1])))
    print('Solution to test input 2 is {}'.format(solve1(test_inputs[3], test_inputs[4])))
    print('Solution to test input 3 is {}'.format(solve1(test_inputs[6], test_inputs[7])))

    input = aoc.read_input('day03.txt')
    print('Solution to part 1 is {}'.format(solve1(input[0], input[1])))


