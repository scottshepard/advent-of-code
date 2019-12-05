import advent_of_code as aoc
import copy
import numpy as np
import pandas as pd
import pdb


class Intcode:

    def __init__(self, instructions):
        self.instructions_raw = instructions
        self.instructions = copy.deepcopy(instructions)
        self.pos = 0
        self.solved = False

    def reset(self):
        self.instructions = copy.deepcopy(self.instructions_raw)
        self.solved = False
        self.pos = 0

    def adjust_input(self, noun_, verb_):
        self.instructions[1] = noun_
        self.instructions[2] = verb_

    def parameter_modes(self, instr):
        instr = str(instr)
        opcode = int(instr[-2:])
        if opcode == 1 or opcode == 2:
            return [int(d) for d in list('0' * (4 - len(str(opcode))) + instr[:-2])], opcode
        elif opcode == 3 or opcode == 4:
            return [int(d) for d in list('0' * (2 - len(str(opcode))) + instr[:-2])], opcode
        elif opcode == 99:
            return [], opcode

    def compute_step(self):
        instructions = self.instructions
        pos = self.pos
        param_modes, opcode = self.parameter_modes(instructions[pos])
        parameters = self.instructions[pos:(pos+len(param_modes))]
        if opcode == 99:
            self.solved = True
            return
        elif opcode == 1:
            instructions[instructions[pos+3]] = instructions[instructions[pos+1]] + instructions[instructions[pos+2]]
            self.pos += 4
        elif opcode == 2:
            opcode[opcode[pos+3]] = opcode[opcode[pos+1]] * opcode[opcode[pos+2]]
            self.pos += 4
        elif opcode == 3:
            opcode[opcode[pos+1]] = opcode[pos+1]
            self.pos += 2


        self.opcode = opcode

if __name__ == '__main__':
    input = aoc.read_input('day05.txt')
    intcode = Intcode(input)



