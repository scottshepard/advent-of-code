import advent_of_code as aoc
import copy
import numpy as np
import pandas as pd
import pdb


class Intcode:

    def __init__(self, codes):
        self.codes_raw = codes
        self.codes = copy.deepcopy(codes)
        self.pos = 0
        self.solved = False

    def reset(self):
        self.codes = copy.deepcopy(self.codes_raw)
        self.solved = False
        self.pos = 0

    def adjust_input(self, noun_, verb_):
        self.codes[1] = noun_
        self.codes[2] = verb_

    def parameter_modes(self, instr):
        instr = str(instr)
        opcode = int(instr[-2:])
        if opcode == 1 or opcode == 2:
            return [int(d) for d in list('0' * (4 - len(str(opcode))) + instr[:-2])], opcode
        elif opcode == 3 or opcode == 4:
            return [int(d) for d in list('0' * (2 - len(str(opcode))) + instr[:-2])], opcode
        elif opcode == 99:
            return [], opcode

    def fetch_param(self, parameter, parameter_mode):
        if parameter_mode == 0:
            return self.codes[parameter]
        elif parameter_mode == 1:
            return parameter

    def compute_step(self, input):
        codes = self.codes
        pos = self.pos
        param_modes, opcode = self.parameter_modes(codes[pos])
        parameters = self.codes[pos:(pos+len(param_modes))]
        if opcode == 99:
            self.solved = True
            return
        elif opcode == 1:
            for p, pm in zip(parameters, param_modes):

            codes[codes[pos+3]] = codes[codes[pos+1]] + codes[codes[pos+2]]
            self.pos += 4
        elif opcode == 2:
            codes[codes[pos+3]] = codes[codes[pos+1]] * codes[codes[pos+2]]
            self.pos += 4
        elif opcode == 3:
            codes[opcode[pos+1]] = codes[input]
            self.pos += 2
        elif opcode == 4:



        self.opcode = opcode

if __name__ == '__main__':
    input = aoc.read_input('day05.txt')
    intcode = Intcode(input)



