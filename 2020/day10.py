from utils import read_input
import numpy as np
import pdb



sample_input = read_input('day10_test.txt')

def solve_part_1(input):
    lst = [int(x) for x in input]
    lst.insert(0, 0)
    lst.append(max(lst)+3)
    lst.sort()
    diffs = []
    i = 0
    while i < len(lst) -1:
        j = i
        while j < len(lst):
            j += 1
            if lst[j] - 3 <= lst[i]:
                diffs.append(lst[i+1] - lst[i])
                i = j
                break
            else:
                j += 1
    a = np.array(diffs)
    unique, counts = np.unique(a, return_counts=True)
    jolts = dict(zip(unique, counts))
    return jolts[1] * jolts[3]

assert solve_part_1(sample_input) == 35

sample_input2 = read_input('day10_test2.txt')
assert solve_part_1(sample_input2) == 220

real_input = read_input('day10.txt')
print('Part 1:', solve_part_1(real_input))
