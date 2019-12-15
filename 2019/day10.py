import copy
import numpy as np
import pandas as pd
from fractions import Fraction
from utils import read_input


class AsteroidBelt:

    def __init__(self, map_input):
        self.map = pd.DataFrame([list(row) for row in map_input])
        self.asteroids = self.find_asteroids()
        self.vaporized = []

    def find_asteroids(self):
        asteroids = {}
        for i, col in self.map.iteritems():
            try:
                j_s = col[col == '#'].index
                for j in j_s:
                    asteroids[(i,j)] = 0
            except:
                pass
        return asteroids

    def is_asteroid_in_los(self, a1, a2, exclude_vaporized=False):
        if exclude_vaporized:
            if self.asteroids[a2] > 0:
                return False
        if a1[0] > a2[0]:
            tmp = copy.deepcopy(a1)
            a1 = copy.deepcopy(a2)
            a2 = tmp
        if a2[0] == a1[0]:
            D = 0
            N = np.sign(a2[1]-a1[1])
        else:
            slope = Fraction(a2[1] - a1[1], a2[0] - a1[0])
            D = slope.denominator
            N = slope.numerator
        s = a2
        s = (s[0] - D, s[1] - N)
        while s != a1:
            if self.map[s[0]][s[1]] == '#':
                return False
            s = (s[0] - D, s[1] - N)
        return True

    def find_asteroids_in_los(self, base, exclude_vaporized=False):
        return [asteroid for asteroid in self.asteroids.keys() if self.is_asteroid_in_los(base, asteroid, exclude_vaporized=exclude_vaporized) and asteroid != base]

    def count_asteroids_in_los(self, base):
        return len(self.find_asteroids_in_los(base))

    def find_best_base(self):
        max_los = 0
        best_asteroid = None
        for asteroid in self.asteroids.keys():
            count_los = self.count_asteroids_in_los(asteroid)
            if count_los > max_los:
                max_los = count_los
                best_asteroid = asteroid
        self.base = best_asteroid
        return best_asteroid

    def solve1(self):
        self.base = self.find_best_base()
        return self.count_asteroids_in_los(self.base)

    def vaporize(self, to_be_vaporized):
        angles = [self.angle(self.base, asteroid) for asteroid in to_be_vaporized]
        sorted_vaporized = [x for _, x in sorted(zip(angles, to_be_vaporized))]
        for ast in sorted_vaporized:
            self.asteroids[ast] += 1
        return sorted_vaporized

    def angle(self, c1, c2):
        raw = np.arctan2(c2[0] - c1[0], -1 * (c2[1] - c1[1]))
        if raw < 0:
            raw += 2 * np.pi
        return raw

    def solve2(self):
        to_be_vaporized = self.find_asteroids_in_los(self.base, exclude_vaporized=True)
        self.vaporized.extend(self.vaporize(to_be_vaporized))
        x, y = self.vaporized[199]
        return x*100+y

if __name__ == '__main__':
    test1 = read_input('day10_test1.txt')
    belt1 = AsteroidBelt(test1)
    assert not belt1.is_asteroid_in_los((0, 4), (0, 0))
    assert belt1.is_asteroid_in_los((4, 0), (1, 0))
    assert belt1.is_asteroid_in_los((4, 0), (4, 2))
    assert not belt1.is_asteroid_in_los((4, 0), (4, 3))
    assert belt1.count_asteroids_in_los((4, 0)) == 7
    assert belt1.count_asteroids_in_los((3, 4)) == 8

    input = read_input('day10.txt')
    belt = AsteroidBelt(input)
    print('Solution to Day 10 part I is {}'.format(belt.solve1()))

    test2 = read_input('day10_test2.txt')
    belt2 = AsteroidBelt(test2)
    belt2.solve1()
    belt2.solve2()

    print('Solution to Day 10 part II is {}'.format(belt.solve2()))
