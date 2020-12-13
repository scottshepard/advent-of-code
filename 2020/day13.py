import math
from utils import read_input
import numpy as np


def solve_part_1(input):
    timestamp = int(input[0])
    min_time = timestamp * 10
    min_bus_id = 0
    for bus_id in input[1].split(','):
        if bus_id == 'x':
            continue
        bus_id = int(bus_id)
        t = math.ceil(timestamp / bus_id) * bus_id
        if t < min_time:
            min_time = t
            min_bus_id = bus_id
    return (min_time % timestamp) * min_bus_id

def chinese_remainder(b_arr, n_arr):
    '''
    Given a vector of bs and ns, what is the x that satisfies the set of equations
    x = b1 (mod n1)
    x = b2 (mod n2)
    x = b3 (mod n3)
    etc..
    '''
    N = np.product(n_arr)
    N_arr = [int(N/n) for n in n_arr]
    x_arr = [pow(x, -1, p) for x, p in zip(N_arr, n_arr)]
    return sum([b*N*x for b, N, x in zip(b_arr, N_arr, x_arr)]) % N

assert chinese_remainder([3,1,6], [5,7,8]) == 78

def solve_part_2(input):
    buses = [(i, int(b)) for i, b, in enumerate(input[1].split(',')) if b !='x']
    b_arr = [bus[0] for bus in buses]
    b_arr = [max(b_arr) - b for b in b_arr]
    n_arr = [bus[1] for bus in buses]
    return chinese_remainder(b_arr, n_arr) - max(b_arr)


sample_input = read_input('day13_test.txt')
assert solve_part_1(sample_input) == 295

real_input = read_input('day13.txt')
print('Part 1:', solve_part_1(real_input))

assert solve_part_2(sample_input) == 1068781
print('Part 2:', solve_part_2(real_input))
