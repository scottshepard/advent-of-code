import re
from utils import read_input
import pdb

class GameConsole:

    def __init__(self, boot_code):
        self.bc = boot_code[:]
        self.acc = 0
        self.i = 0

    def execute_line(self):
        instr = self.bc[self.i]
        op, arg = tuple(instr.split(' '))
        arg = int(arg)
        if op == 'jmp':
            self.i += arg
        elif op == 'acc':
            self.i += 1
            self.acc += arg
        elif op == 'nop':
            self.i += 1

    def execute(self):
        solved = False
        instr_run = []
        while not solved:
            instr_run.append(self.i)
            self.execute_line()
            if self.i in instr_run:
                solved = True
                repeating = True
            if self.i >= len(self.bc):
                solved = True
                repeating = False
        return self.acc, repeating


def solve_part_1(input_):
    gc = GameConsole(input_)
    acc, _ = gc.execute()
    return acc

def solve_part_2(input):
    repeating = True
    j = 0
    while repeating:
        input_ = input[:]
        arg = input[j].split(' ')[0]
        if arg == 'nop':
            input_[j] = re.sub('nop', 'jmp', input_[j])
        if arg == 'jmp':
            input_[j] = re.sub('jmp', 'nop', input_[j])
        gc = GameConsole(input_)
        # pdb.set_trace()
        acc, repeating = gc.execute()
        j += 1
    return acc



sample_input = read_input('day08_test.txt')
assert solve_part_1(sample_input) == 5
assert solve_part_2(sample_input) == 8


real_input = read_input('day08.txt')
print('Part 1:', solve_part_1(real_input))
print('Part 2:', solve_part_2(real_input))


