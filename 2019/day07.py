import advent_of_code as aoc
import copy
from itertools import permutations
import pandas as pd
import pdb


class IntcodeComputer:

    def __init__(self, input):
        self.input = copy.deepcopy(input)
        self.reset()

    def reset(self):
        self.codes = [int(x) for x in self.input.split(',')]
        self.solved = False
        self.pos = 0
        self.outputs = []
        self.output = None

    def adjust_input(self, noun_, verb_):
        self.codes[1] = noun_
        self.codes[2] = verb_

    def parameter_modes(self, instr):
        instr = str(instr)
        opcode = int(instr[-2:])
        if opcode in [1,2,7,8]:
            return [int(d) for d in list('0' * (3 - len(instr[:-2])) + instr[:-2])], opcode
        elif opcode in [3,4]:
            return [int(d) for d in list('0' * (1 - len(instr[:-2])) + instr[:-2])], opcode
        elif opcode == 99:
            return [], opcode
        elif opcode in [5,6]:
            return [int(d) for d in list('0' * (2 - len(instr[:-2])) + instr[:-2])], opcode

    def fetch_param(self, parameter, parameter_mode):
        if parameter_mode == 0:
            return self.codes[parameter]
        elif parameter_mode == 1:
            return parameter

    def param_values(self, parameters, param_modes):
        values = []
        for p, pm in zip(parameters, param_modes):
            values.append(self.fetch_param(p, pm))
        return values

    def compute_step(self, input=None):
        '''
        :param input: An int to get things rolling
        Opcode 1 adds together numbers read from two positions and stores the result in a third position.
            The three integers immediately after the opcode tell you these three positions -
            the first two indicate the positions from which you should read the input values,
            and the third indicates the position at which the output should be stored.
            For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20,
            add those values, and then overwrite the value at position 30 with their sum.
        Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
            Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.
        Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
            For example, the instruction 3,50 would take an input value and store it at address 50.
        Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at
            address 50.
        Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value
            from the second parameter. Otherwise, it does nothing.
        Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from
            the second parameter. Otherwise, it does nothing.
        Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position
            given by the third parameter. Otherwise, it stores 0.
        Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given
            by the third parameter. Otherwise, it stores 0.
        '''
        codes = self.codes
        pos = self.pos
        # pdb.set_trace()
        param_modes, opcode = self.parameter_modes(codes[pos])
        param_modes.reverse()
        parameters = self.codes[(pos+1):(pos+1+len(param_modes))]
        # pdb.set_trace()
        if opcode == 99:
            self.solved = True
        elif opcode == 1:
            values = self.param_values(parameters, param_modes)
            codes[codes[pos+3]] = values[0] + values[1]
            self.pos += 4
        elif opcode == 2:
            values = self.param_values(parameters, param_modes)
            codes[codes[pos+3]] = values[0] * values[1]
            self.pos += 4
        elif opcode == 3:
            codes[codes[pos+1]] = input
            self.pos += 2
        elif opcode == 4:
            value = self.fetch_param(parameters[0], param_modes[0])
            self.outputs.append(value)
            self.pos += 2
        elif opcode == 5:
            values = self.param_values(parameters, param_modes)
            if values[0] != 0:
                self.pos = values[1]
            else:
                self.pos += 3
        elif opcode == 6:
            values = self.param_values(parameters, param_modes)
            if values[0] == 0:
                self.pos = values[1]
            else:
                self.pos += 3
        elif opcode == 7:
            values = self.param_values(parameters, param_modes)
            if values[0] < values[1]:
                codes[codes[pos+3]] = 1
            else:
                codes[codes[pos + 3]] = 0
            self.pos += 4
        elif opcode == 8:
            values = self.param_values(parameters, param_modes)
            if values[0] == values[1]:
                codes[codes[pos+3]] = 1
            else:
                codes[codes[pos + 3]] = 0
            self.pos += 4

    def solve(self, i1=None, i2=None):
        self.compute_step(i1)
        while not self.solved:
            self.compute_step(i2)
        if len(self.outputs) > 0:
            self.output = self.outputs[-1]
        return self.output


class AmplifierChain:

    def __init__(self, control_software, n_amplifiers=5):
        self.n_amplifiers = n_amplifiers
        self.acs_raw = copy.deepcopy(control_software)
        self.reset()

    def reset(self):
        self.acs = copy.deepcopy(self.acs_raw)
        self.amplifiers = [IntcodeComputer(self.acs) for x in range(self.n_amplifiers)]

    def thruster_signal(self, phase_setting, first_input=0):
        self.reset()
        amp_out = first_input
        i = 0
        for amp in self.amplifiers:
            amp_out = amp.solve(phase_setting[i], amp_out)
            i += 1
        return amp_out

    def find_max_thruster_signal(self, signal_digits=[0,1,2,3,4]):
        self.reset()
        self.thruster_signals = []
        perms = permutations(signal_digits)
        for perm in list(perms):
            self.thruster_signals.append(self.thruster_signal(perm))
        return pd.Series(self.thruster_signals).max()




if __name__ == '__main__':
    acs_test = aoc.read_input('day07_test.txt')

    phase_setting = [4,3,2,1,0]
    A = IntcodeComputer(acs_test[0])
    A.solve(phase_setting[0], 0)

    B = IntcodeComputer(acs_test[0])
    B.solve(phase_setting[1], A.output)

    C = IntcodeComputer(acs_test[0])
    C.solve(phase_setting[2], B.output)

    D = IntcodeComputer(acs_test[0])
    D.solve(phase_setting[3], C.output)

    E = IntcodeComputer(acs_test[0])
    E.solve(phase_setting[4], D.output)

    assert E.output == 43210

    ac0 = AmplifierChain(acs_test[0])
    assert ac0.thruster_signal([4,3,2,1,0]) == 43210

    ac1 = AmplifierChain(acs_test[1])
    assert ac1.thruster_signal([0,1,2,4,3]) != 54321

    ac2 = AmplifierChain(acs_test[2])
    assert ac2.find_max_thruster_signal() == 65210

    # For real now
    acs = aoc.read_input('day07.txt')[0]
    ac = AmplifierChain(acs)
    print('Solution to Day 7 Part I is {}'.format(ac.find_max_thruster_signal()))
