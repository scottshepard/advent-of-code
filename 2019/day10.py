import advent_of_code as aoc
import copy
import numpy as np
import pandas as pd
from fractions import Fraction
import pdb


class AsteroidBelt:

    def __init__(self, map_input):
        self.map = pd.DataFrame([list(row) for row in map_input])
        self.asteroids = self.find_asteroids()

    def find_asteroids(self):
        asteroids = {}
        for i, col in self.map.iteritems():
            try:
                j_s = col[col == '#'].index
                for j in j_s:
                    asteroids[(j,i)] = 0
            except:
                pass
        return asteroids

    def is_asteroid_in_los(self, a1, a2):
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
        search = a2
        search = (search[0] - D, search[1] - N)
        while search != a1:
            if self.map.loc[search] == '#':
                return False
            search = (search[0] - D, search[1] - N)
        return True

    def count_asteroids_in_los(self, base):
        return pd.Series([1 if self.is_asteroid_in_los(base, asteroid) else 0 for asteroid in self.asteroids.keys()]).sum() - 1

    def find_best_base(self):
        max_los = 0
        best_asteroid = None
        for asteroid in self.asteroids.keys():
            count_los = self.count_asteroids_in_los(asteroid)
            if count_los > max_los:
                max_los = count_los
                best_asteroid = asteroid
            self.asteroids[asteroid] = count_los
        return best_asteroid, max_los




if __name__ == '__main__':
    test1 = aoc.read_input('day10_test1.txt')
    belt = AsteroidBelt(test1)
    assert belt.is_asteroid_in_los((0, 4), (0, 1))
    assert belt.is_asteroid_in_los((0, 4), (2, 4))
    assert not belt.is_asteroid_in_los((0, 4), (3, 4))
    assert belt.count_asteroids_in_los((0, 4)) == 7
    assert belt.count_asteroids_in_los((4, 3)) == 8
    assert belt.find_best_base() == ((4,3), 8)
