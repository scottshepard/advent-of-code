import re
from itertools import combinations
from utils import read_input


def parse_input(lines):
    x, y, z = [], [], []
    for line in lines:
        ints = [int(i) for i in re.findall(r'-?[0-9]+', line)]
        x.append(ints[0])
        y.append(ints[1])
        z.append(ints[2])
    return x, y, z

def update_axis(axis, velocity, index_pairs):
    axis, velocity
    for ip in index_pairs:
        if axis[ip[0]] > axis[ip[1]]:
            velocity[ip[0]] -= 1
            velocity[ip[1]] += 1
        elif axis[ip[0]] < axis[ip[1]]:
            velocity[ip[0]] += 1
            velocity[ip[1]] -= 1
    for i in range(len(axis)):
        axis[i] += velocity[i]
    return axis, velocity

def update_system(axes, velocities):
    axes = list(axes)
    velocities = list(velocities)
    index_pairs = [index for index in combinations(range(4), 2)]
    for i in range(len(axes)):
        axes[i], velocities[i] = update_axis(axes[i], velocities[i], index_pairs)
    return axes, velocities

def total_energy(axes, velocities):
    total = 0
    for j in range(len(axes[0])):
        planet_pot = 0
        planet_kin = 0
        for i in range(len(axes)):
            planet_pot += abs(axes[i][j])
            planet_kin += abs(velocities[i][j])
            #pdb.set_trace()
        total += planet_pot * planet_kin
    return total


if __name__ == '__main__':

    test_input1 = read_input('day12_test1.txt')
    velocities1 = [0,0,0,0], [0,0,0,0], [0,0,0,0]
    positions1 = parse_input(test_input1)

    for i in range(10):
        positions1, velocities1 = update_system(positions1, velocities1)
    assert total_energy(positions1, velocities1) == 179

    test_input2 = read_input('day12_test2.txt')
    velocities2 = [0,0,0,0], [0,0,0,0], [0,0,0,0]
    positions2 = parse_input(test_input2)

    for i in range(100):
        positions, velocities = update_system(positions2, velocities2)
    assert total_energy(positions2, velocities2) == 1940

    input = read_input('day12.txt')
    velocities = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    positions = parse_input(input)

    for i in range(1000):
        positions, velocities = update_system(positions, velocities)
    print("Solution to Day 12 Part I is {}".format(total_energy(positions, velocities)))

