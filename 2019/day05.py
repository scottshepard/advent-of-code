import copy
from utils import read_input


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

    def solve(self, input=None):
        while not self.solved:
            self.compute_step(input)
        if len(self.outputs) > 0:
            self.output = self.outputs[-1]
        return self.output


if __name__ == '__main__':
    input = read_input('day05.txt')[0]
    ic = IntcodeComputer(input)

    assert ic.parameter_modes(1002) == ([0, 1, 0], 2)
    assert ic.parameter_modes(1101) == ([0, 1, 1], 1)
    assert ic.parameter_modes(1) == ([0, 0, 0], 1)
    assert ic.parameter_modes(3) == ([0], 3)

    param_modes, opcode = ic.parameter_modes(ic.codes[ic.pos])
    parameters = ic.codes[(ic.pos+1):(ic.pos+1+len(param_modes))]

    ic_test1 = IntcodeComputer('3,0,4,0,99')
    assert ic_test1.solve(10) == 10

    ic_test2 = IntcodeComputer('1101,100,-1,4,0')
    ic_test2.solve()
    assert ic_test2.outputs == []
    assert ic_test2.codes == [1101,100,-1,4,99]

    print('Solution to Day 5 part 1 is {}'.format(ic.solve(1)))

    assert ic.output == 14155342
    ic.reset()
    assert ic.input == input

    test_inputs = read_input('day05_test.txt')

    # Test input 0 should test if input is equal to 8. 1 if true, 0 if false
    x = IntcodeComputer(test_inputs[0])
    assert x.solve(1) == 0
    x.reset()
    assert x.solve(8) == 1

    # Test input 1 should test if input is less than 8. 1 if true, 0 if false
    x = IntcodeComputer(test_inputs[1])
    assert x.solve(1) == 1
    x.reset()
    assert x.solve(8) == 0
    x.reset()
    assert x.solve(9) == 0

    # Test input 2 should test if input is less than 8. 1 if true, 0 if false
    x = IntcodeComputer(test_inputs[2])
    assert x.solve(8) == 1
    x.reset()
    assert x.solve(3) == 0
    x.reset()
    assert x.solve(100) == 0

    # Test input 3 should test if input is less than 8. 1 if true, 0 if false
    x = IntcodeComputer(test_inputs[3])
    assert x.solve(7) == 1
    x.reset()
    assert x.solve(80) == 0

    # Test inputs 4 and 5 take an input, output 0 if input is 0 and 1 otherwise
    x = IntcodeComputer(test_inputs[4])
    assert x.solve(0) == 0
    x.reset()
    assert x.solve(1) == 1
    x.reset()
    assert x.solve(10) == 1


    # This example program uses an input instruction to ask for a single number.
    # The program will then output 999 if the input value is below 8,
    # output 1000 if the input value is equal to 8,
    # or output 1001 if the input value is greater than 8.
    x = IntcodeComputer(test_inputs[-1])
    assert x.solve(7) == 999
    x.reset()
    assert x.solve(8) == 1000
    x.reset()
    assert x.solve(100) == 1001
    ic.reset()

    print('Solution to Day 5 part 2 is {}'.format(ic.solve(5)))
