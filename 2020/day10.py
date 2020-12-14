from utils import read_input
import numpy as np
import pdb



sample_input = read_input('day10_test.txt')

def count_diffs(input):
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
    return diffs

def value_counts(lst):
    unique, counts = np.unique(lst, return_counts=True)
    return dict(zip(unique, counts))


def solve_part_1(input):
    diffs = count_diffs(input)
    jolts = value_counts(diffs)
    return jolts[1] * jolts[3]

assert solve_part_1(sample_input) == 35

sample_input2 = read_input('day10_test2.txt')
assert solve_part_1(sample_input2) == 220

real_input = read_input('day10.txt')
print('Part 1:', solve_part_1(real_input))

def solve_part_2(input):
    diffs = count_diffs(input)
    diffs.insert(0, 3)
    pattern = []
    for i, d in enumerate(diffs):
        if d == 1:
            continue
        else:
            count_1s = 0
            j = 1
            while (i+j < len(diffs) and (diffs[i+j] == 1)):
                j += 1
                count_1s += 1
            pattern.append(count_1s)
    P = value_counts(pattern)
    if 4 not in P.keys():
        P[4] = 0
    return 2**P[2] * 4**P[3] * 7**P[4]

assert solve_part_2(sample_input) == 8
assert solve_part_2(sample_input2) == 19208

print('Part 2:', solve_part_2(real_input))
