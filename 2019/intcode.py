from utils import read_input
import copy

class IntcodeComputer:

    def __init__(self, source, phase_setting=None):
        self.source_raw = copy.deepcopy(source)
        self.reset()
        self.phase_setting = phase_setting
        if phase_setting is not None:
            self.inputs.append(phase_setting)
            self.compute_step()

    def reset(self):
        self.source_code = [int(x) for x in self.source_raw.split(',')]
        self.solved = False
        self.halt = False
        self.pos = 0
        self.inputs =[]
        self.outputs = []
        self.output = None

    def adjust_input(self, noun_, verb_):
        self.source_code[1] = noun_
        self.source_code[2] = verb_

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
            return self.source_code[parameter]
        elif parameter_mode == 1:
            return parameter

    def param_values(self, parameters, param_modes):
        values = []
        for p, pm in zip(parameters, param_modes):
            values.append(self.fetch_param(p, pm))
        return values

    def compute_step(self):
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
            given by the third parameter. Otherwise, codit stores 0.
        Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given
            by the third parameter. Otherwise, it stores 0.
        '''
        pos = self.pos
        param_modes, opcode = self.parameter_modes(self.source_code[pos])
        param_modes.reverse()
        parameters = self.source_code[(pos+1):(pos+1+len(param_modes))]
        # pdb.set_trace()
        if opcode == 99:
            self.solved = True
            self.halt = True
        elif opcode == 1:
            values = self.param_values(parameters, param_modes)
            self.source_code[self.source_code[pos+3]] = values[0] + values[1]
            self.pos += 4
        elif opcode == 2:
            values = self.param_values(parameters, param_modes)
            self.source_code[self.source_code[pos+3]] = values[0] * values[1]
            self.pos += 4
        elif opcode == 3:
            if len(self.inputs) > 0:
                input = self.inputs.pop(0)
            else:
                self.halt = True
                return
            self.source_code[self.source_code[pos+1]] = input
            self.pos += 2
        elif opcode == 4:
            value = self.fetch_param(parameters[0], param_modes[0])
            self.pos += 2
            self.outputs.append(value)
            self.output = value
            return value
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
                self.source_code[self.source_code[pos+3]] = 1
            else:
                self.source_code[self.source_code[pos + 3]] = 0
            self.pos += 4
        elif opcode == 8:
            values = self.param_values(parameters, param_modes)
            if values[0] == values[1]:
                self.source_code[self.source_code[pos+3]] = 1
            else:
                self.source_code[self.source_code[pos + 3]] = 0
            self.pos += 4

    def next(self, inputs=[]):
        self.halt = False
        self.inputs = inputs
        while not self.halt:
            self.compute_step()
        return self.outputs, self.solved


class AmplifierChain:

    def __init__(self, control_software, n_amplifiers=5, phase_setting=None):
        self.n_amplifiers = n_amplifiers
        self.acs_raw = copy.deepcopy(control_software)
        self.reset(phase_setting)

    def reset(self, phase_setting=None):
        self.acs = copy.deepcopy(self.acs_raw)
        self.amplifiers = []
        for x in range(self.n_amplifiers):
            if phase_setting is None:
                ps = None
            else:
                ps = phase_setting[x]
            self.amplifiers.append(IntcodeComputer(self.acs, x))

    def thruster_signal(self, phase_setting, first_input=0):
        self.reset(phase_setting)
        amp_out = first_input
        i = 0
        for amp in self.amplifiers:
            amp_out = amp.solve(phase_setting[i], amp_out)
            i += 1
        return amp_out

    def thruster_signal2(self, first_input=0):
        self.reset(phase_setting)
        amp_out = first_input
        solved = False
        i = 0
        while not solved:
            amp = self.amplifiers[i % 5]
            amp_out, solved = amp.next(amp_out)
            i += 1
        return amp_out

    def find_max_thruster_signal(self, signal_digits=[0,1,2,3,4]):
        self.reset()
        self.thruster_signals = []
        perms = permutations(signal_digits)
        for perm in list(perms):
            self.thruster_signals.append(self.thruster_signal(perm))
        return pd.Series(self.thruster_signals).max()


class TestIntcodeComputer:

    def test_opcodes_1_2():
        A = IntcodeComputer('1,9,10,3,2,3,11,0,99,30,40,50')

        # Intcode A tests opcode 1, 2 then stops
        # Test Opcode 1
        A.compute_step()
        assert A.source_code == [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert A.solved == False
        # Test Opcode 2
        A.compute_step()
        assert A.source_code == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert A.solved == False
        # Should be done now
        A.compute_step()
        assert A.source_code == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert A.solved

        # Now using the "next" function which should iterate until it reaches
        # An input instruction with no input or a stop command.
        A = IntcodeComputer('1,9,10,3,2,3,11,0,99,30,40,50')
        assert A.source_code == [1,9,10,3,2,3,11,0,99,30,40,50]
        assert A.solved == False
        # Test Opcode 2
        A.next()
        assert A.source_code == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert A.solved

        # Intcode B adds 1 to 1 then stops
        B = IntcodeComputer('1,0,0,0,99')
        B.compute_step()
        assert B.source_code == [2, 0, 0, 0, 99]
        assert B.solved == False
        B.compute_step()
        assert B.solved

        # Intcode C multiplies 3 * 2 then stops
        C = IntcodeComputer('2,3,0,3,99')
        C.compute_step()
        assert C.source_code == [2, 3, 0, 6, 99]
        C.compute_step()
        assert C.solved

        # Intcode D multiplies 99 * 99 then stops
        D = IntcodeComputer('2,4,4,5,99,0')
        D.compute_step()
        assert D.source_code == [2, 4, 4, 5, 99, 9801]
        D.compute_step()
        assert D.solved

        # Intcode E performs two operations and then stops
        E = IntcodeComputer('1,1,1,4,99,5,6,0,99')
        E = IntcodeComputer('1,1,1,4,99,5,6,0,99')
        E.compute_step()
        assert E.source_code == [1, 1, 1, 4, 2, 5, 6, 0, 99]
        E.compute_step()
        assert E.source_code == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    def test_opcodes_3_4():
        # Test 3 & 4. Opcode A should output what is input and then stop.
        A = IntcodeComputer('3,0,4,0,99')
        A.inputs = [10]
        A.compute_step()
        assert A.source_code == [10, 0, 4, 0, 99]
        x = A.compute_step()
        assert x == 10
        A.compute_step()
        assert A.solved
        A.compute_step()
        assert A.solved

        A = IntcodeComputer('3,0,4,0,99')
        A.next([10])
        assert A.source_code == [10, 0, 4, 0, 99]
        assert A.outputs == [10]
        assert A.solved

        B = IntcodeComputer('1101,100,-1,4,0')
        B.compute_step()
        assert B.source_code == [1101, 100, -1, 4, 99]
        assert B.pos == 4
        assert B.solved == False
        B.compute_step()
        assert B.solved

        # Test Day 5 input
        C = IntcodeComputer('3,7,1,8,6,6,1100,1,238,225', 101)
        C.compute_step()
        assert C.source_code == [3, 7, 1, 8, 6, 6, 1338, 101, 238, 225]
        C = IntcodeComputer(read_input('day05.txt')[0], 1)
        C.next()
        assert C.output == 14155342


if __name__ == '__main__':
    import pdb

    TestIntcodeComputer.test_opcodes_1_2()
    TestIntcodeComputer.test_opcodes_3_4()



