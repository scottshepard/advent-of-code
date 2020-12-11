from itertools import combinations
from utils import read_input
import pdb


def weak_xmas(data, n):
    data = [int(d) for d in data]

    def contains_sum(pre, x):
        for c in combinations(pre, 2):
            if sum(c) == x:
                return True
        return False

    preamble = data[:n]
    for i in range(n, len(data)):
        if not contains_sum(preamble, data[i]):
            return data[i]
        #pdb.set_trace()
        preamble = data[(i-n+1):(i+1)]

def continuous_set(data, target):
    data = [int(d) for d in data]
    for i in range(len(data)):
        for j in range(i, len(data)):
            if sum(data[i:j]) == target:
                return data[i:j]

sample_input = read_input('day09_test.txt')
assert weak_xmas(sample_input, 5) == 127

real_input = read_input('day09.txt')
print('Part 1:', weak_xmas(real_input, 25))

assert continuous_set(sample_input, 127) == [15, 25, 47, 40]

x = continuous_set(real_input, weak_xmas(real_input, 25))
print('Part 2:', min(x) + max(x))
