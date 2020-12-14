from utils import read_input
import re
import pdb

def apply_mask(mask, value):
    bin_val = bin(value)[2:].rjust(36, '0')
    output = []
    for b, m in zip(bin_val, mask):
        if m == 'X':
            output.append(b)
        else:
            output.append(m)
    output = ''.join(output)
    return int(output, 2)

sample_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'

assert apply_mask(sample_mask, 11) == 73
assert apply_mask(sample_mask, 101) == 101


sample_input = read_input('day14_test.txt')


def solve_part_1(input):
    mem = {}
    for line in input:
        if line[:4] == 'mask':
            mask = line[7:]
        else:
            matches = re.findall('[0-9]+', line)
            #pdb.set_trace()
            mem[matches[0]] = apply_mask(mask, int(matches[1]))
    return sum(mem.values())

assert solve_part_1(sample_input) == 165

real_input = read_input('day14.txt')
print('Part 1:', solve_part_1(real_input))

