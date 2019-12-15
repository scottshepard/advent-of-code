import copy
import pandas as pd
from utils import read_input


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
            total_orbits += len(self.orbits_for_planet(planet, []))
        return total_orbits

    def orbits_for_planet(self, planet, planets_list=[], stop=''):
        if planet in self.map.keys() and planet != stop:
            planets_list.append(planet)
            return self.orbits_for_planet(self.map[planet], planets_list, stop)
        else:
            return planets_list

    def orbital_transfer_count(self, p1, p2):
        san = self.orbits_for_planet(p1, [])
        you = self.orbits_for_planet(p2, [])
        intersections = set(san).intersection(set(you))
        return pd.Series([san.index(inter) + you.index(inter) for inter in intersections]).min() -2



if __name__ == '__main__':
    test_input = read_input('day06_test.txt')
    t_ss = SolarSystem(test_input)
    assert(t_ss.count_orbits_in_system()==42)

    input = read_input('day06.txt')
    ss = SolarSystem(input)
    print('Solution to part 1 is {}'.format(ss.count_orbits_in_system()))

    test_input2 = read_input('day06_test2.txt')
    t_ss2 = SolarSystem(test_input2)
    assert(t_ss2.orbital_transfer_count('SAN', 'YOU')==4)

    print('Solution to part 2 is {}'.format(ss.orbital_transfer_count('SAN', 'YOU')))
