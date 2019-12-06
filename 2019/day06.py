import advent_of_code as aoc
import copy
import numpy as np
import pandas as pd
import pdb

class SolarSystem:

    def __init__(self, map):
        self.map_raw = copy.deepcopy(map)
        self.map = self.parse_map()

    def parse_map(self):
        map = {}
        for orbit in self.map_raw:
            x, y = self.parse_orbit(orbit)
            map[y] = x
        return map

    def parse_orbit(self, orbit):
        orbit = orbit.split(')')
        return orbit[0], orbit[1]

    def count_orbits_in_system(self):
        total_orbits = 0
        for planet in self.map.keys():
            total_orbits += self.count_orbits_for_planet(planet)
        return total_orbits

    def count_orbits_for_planet(self, planet, orbits=0):
        if planet in self.map.keys():
            return self.count_orbits_for_planet(self.map[planet], orbits+1)
        else:
            return orbits




if __name__ == '__main__':
    test_input = aoc.read_input('day06_test.txt')
    test_ss = SolarSystem(test_input)
    assert(test_ss.count_orbits_in_system()==42)

    input = aoc.read_input('day06.txt')
    ss = SolarSystem(input)
    print('Solution to part 1 is {}'.format(ss.count_orbits_in_system()))


