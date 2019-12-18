import re
import numpy as np
from itertools import combinations
from utils import read_input


class System:

    def __init__(self, lines):
        self.lines = lines
        self.axes_raw = self.parse_input(lines)
        self.axes = self.parse_input(lines)
        self.vels = {'X': [0]*4, 'Y': [0]*4, 'Z': [0]*4}
        self.index_pairs = [index for index in combinations(range(4), 2)]

    def parse_input(self, lines):
        x, y, z = [], [], []
        for line in lines:
            ints = [int(i) for i in re.findall(r'-?[0-9]+', line)]
            x.append(ints[0])
            y.append(ints[1])
            z.append(ints[2])
        return {'X': x, 'Y': y, 'Z': z}

    def update_axis(self, axis_name):
        axis = self.axes[axis_name]
        vel = self.vels[axis_name]
        for ip in self.index_pairs:
            if axis[ip[0]] > axis[ip[1]]:
                vel[ip[0]] -= 1
                vel[ip[1]] += 1
            elif axis[ip[0]] < axis[ip[1]]:
                vel[ip[0]] += 1
                vel[ip[1]] -= 1
        for i in range(len(axis)):
            axis[i] += vel[i]
        self.axes[axis_name] = axis
        self.vels[axis_name] = vel

    def update_system(self, steps=1):
        for n in range(steps):
            for a in ['X', 'Y', 'Z']:
                self.update_axis(a)

    def total_energy(self):
        total = 0
        for i in range(4):
            planet_pot = 0
            planet_kin = 0
            for a in ['X', 'Y', 'Z']:
                planet_pot += abs(self.axes[a][i])
                planet_kin += abs(self.vels[a][i])
            total += planet_pot * planet_kin
        return total

    def find_axis_repitition_steps(self, axis_name):
        steps = 1
        self.update_axis(axis_name)
        while self.axes[axis_name] != self.axes_raw[axis_name] or self.vels[axis_name] != [0,0,0,0]:
            self.update_axis(axis_name)
            steps += 1
        return steps

    def find_system_repitiion_steps(self):
        x = self.find_axis_repitition_steps('X')
        y = self.find_axis_repitition_steps('Y')
        z = self.find_axis_repitition_steps('Z')
        return np.lcm.reduce([x,y,z])


if __name__ == '__main__':

    test_input1 = read_input('day12_test1.txt')
    S1 = System(test_input1)
    S1.update_system(10)
    assert S1.total_energy() == 179

    test_input2 = read_input('day12_test2.txt')
    S2 = System(test_input2)
    S2.update_system(100)
    assert S2.total_energy() == 1940

    input = read_input('day12.txt')
    S = System(input)
    S.update_system(1000)
    print('Solution to Day 12 Part I is {}'.format(S.total_energy()))

    S1 = System(test_input1)
    assert S1.find_system_repitiion_steps() == 2772

    S = System(input)
    print('Solution to Day 12 Part II is {}'.format(S.find_system_repitiion_steps()))
