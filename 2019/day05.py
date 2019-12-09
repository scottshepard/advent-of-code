import advent_of_code as aoc
import copy
import numpy as np
import pandas as pd
import pdb


class IntcodeComputer:

    def __init__(self, input):
        self.input = copy.deepcopy(input)
        self.codes = [int(x) for x in input.split(',')]
        self.pos = 0
        self.solved = False

    def reset(self):
        self.codes = copy.deepcopy(self.input)
        self.solved = False
        self.pos = 0

    def adjust_input(self, noun_, verb_):
        self.codes[1] = noun_
        self.codes[2] = verb_

    def parameter_modes(self, instr):
        instr = str(instr)
        opcode = int(instr[-2:])
        if opcode == 1 or opcode == 2:
            return [int(d) for d in list('0' * (5 - len(instr)) + instr[:-2])], opcode
        elif opcode == 3 or opcode == 4:
            return [int(d) for d in list('0' * (2 - len(instr)) + instr[:-2])], opcode
        elif opcode == 99:
            return [], opcode

    def fetch_param(self, parameter, parameter_mode):
        if parameter_mode == 0:
            return self.codes[parameter]
        elif parameter_mode == 1:
            return parameter

    def compute_step(self, input=None):
        codes = self.codes
        pos = self.pos
        param_modes, opcode = self.parameter_modes(codes[pos])
        parameters = self.codes[(pos+1):(pos+1+len(param_modes))]
        if opcode == 99:
            self.solved = True
        elif opcode == 1:
            values = []
            for p, pm in zip(parameters, param_modes):
                values.append(self.fetch_param(p, pm))
            codes[codes[pos+3]] = values[0] + values[1]
            self.pos += 4
        elif opcode == 2:
            values = []
            for p, pm in zip(parameters, param_modes):
                values.append(self.fetch_param(p, pm))
            codes[codes[pos+3]] = values[0] * values[1]
            self.pos += 4
        elif opcode == 3:
            codes[opcode[pos+1]] = codes[input]
            self.pos += 2
        elif opcode == 4:
            value = self.fetch_param(parameters[0], param_modes[0])
            self.pos += 2
            return value


if __name__ == '__main__':
    input = aoc.read_input('day05.txt')[0]
    ic = IntcodeComputer(input)
    assert(ic.parameter_modes(1002) == ([0, 1, 0], 2))
    assert(ic.parameter_modes(1101) == ([0, 1, 1], 1))
    assert(ic.parameter_modes(3) == ([0], 3))

    '1101, 100, -1, 4, 0'

    param_modes, opcode = ic.parameter_modes(ic.codes[ic.pos])
    parameters = ic.codes[(ic.pos+1):(ic.pos+1+len(param_modes))]

    test_input = '3,0,4,0,99'
    ic_test = IntcodeComputer(test_input)



