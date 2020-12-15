from utils import read_input
import re


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

sample_input = read_input('day14_test.txt')
assert solve_part_1(sample_input) == 165

real_input = read_input('day14.txt')
print('Part 1:', solve_part_1(real_input))


def apply_mask2(mask, mem):
    mem_val = bin(mem)[2:].rjust(36, '0')
    output = [[]]
    for b, m in zip(mem_val, mask):
        if m == 'X':
            res = []
            for i in range(len(output)):
                lst0 = output[i].copy()
                lst0.append('0')
                lst1 = output[i].copy()
                lst1.append('1')
                res.append(lst0)
                res.append(lst1)
            output = res
        elif m == '1':
            for o in output:
                o.append('1')
        elif m == '0':
            for o in output:
                o.append(b)
    return [int(''.join(o),2) for o in output]

assert apply_mask2('000000000000000000000000000000X1001X', 42) == [26, 27, 58, 59]

def solve_part_2(input):
    mem = {}
    for line in input:
        if line[:4] == 'mask':
            mask = line[7:]
        else:
            matches = re.findall('[0-9]+', line)
            #pdb.set_trace()
            addresses = apply_mask2(mask, int(matches[0]))
            for a in addresses:
                mem[a] = int(matches[1])
    return sum(mem.values())

sample_input2 = read_input('day14_test2.txt')
assert solve_part_2(sample_input2)

print('Part 2:', solve_part_2(real_input))
