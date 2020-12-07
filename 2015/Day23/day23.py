import os
import pdb


def read_input(file, split_char='\n'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    f = open(file_path)
    data = f.read().split(split_char)
    if data[-1] == '':
        data.pop(-1)
    return data


def solve(instr, a=0, b=0):
    i = 0
    registers = {'a':a, 'b':b}
    while i < len(instr):
        line = instr[i]
        reg = line.split(' ')[1]
        #pdb.set_trace()
        if line[:3] == 'hlf':
            registers[reg] = registers[reg]/2
            i += 1
        elif line[:3] == 'tpl':
            registers[reg] = registers[reg]*3
            i += 1
        elif line[:3] == 'inc':
            registers[reg] += 1
            i += 1
        elif line[:3] == 'jmp':
            i += int(reg)
        elif line[:3] == 'jie':
            if registers[reg[0]] % 2 == 0:
                i += int(line.split(' ')[-1])
            else:
                i += 1
        elif line[:3] == 'jio':
            if registers[reg[0]] == 1:
                i += int(line.split(' ')[-1])
            else:
                i += 1
    return registers


input = read_input('day23.txt')
sample_input = read_input('day23_test.txt')

assert solve(sample_input) == {'a':2, 'b':0}
print('Part 1:', solve(input)['b'])
print('Part 2:', solve(input, 1)['b'])

# 50 is incorrect
