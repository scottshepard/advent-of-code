from utils import read_input
import copy

class IntcodeComputer:

    def __init__(self, source, phase_setting=None):
        self.source_raw = copy.deepcopy(source)
        self.source_code = self.source_code_dict(self.source_raw)
        self.solved = False
        self.halt = False
        self.pos = 0
        self.relative_base = 0
        self.inputs =[]
        self.outputs = []
        self.output = None
        self.phase_setting = phase_setting
        if phase_setting is not None:
            self.inputs.append(phase_setting)
            self.compute_step()

    def source_code_dict(self, source_code_raw):
        source_code_list = [int(x) for x in self.source_raw.split(',')]
        source_code_dict = {}
        for i in range(len(source_code_list)):
            source_code_dict[i] = source_code_list[i]
        return source_code_dict

    def adjust_input(self, noun_, verb_):
        self.source_code[1] = noun_
        self.source_code[2] = verb_

    def parameter_modes(self, instr):
        instr = str(instr)
        opcode = int(instr[-2:])
        if opcode in [1,2,7,8]:
            return [int(d) for d in list('0' * (3 - len(instr[:-2])) + instr[:-2])], opcode
        elif opcode in [3,4,9]:
            return [int(d) for d in list('0' * (1 - len(instr[:-2])) + instr[:-2])], opcode
        elif opcode == 99:
            return [], opcode
        elif opcode in [5,6]:
            return [int(d) for d in list('0' * (2 - len(instr[:-2])) + instr[:-2])], opcode

    def fetch_param(self, parameter, parameter_mode):
        if parameter_mode == 0:
            if parameter > max(list(self.source_code.keys())):
                return 0
            else:
                return self.source_code[parameter]
        elif parameter_mode == 1:
            return parameter
        elif parameter_mode == 2:
            if parameter + self.relative_base > max(list(self.source_code.keys())):
                return 0
            else:
                return self.source_code[parameter + self.relative_base]

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
        parameters = [self.source_code[i] for i in range(pos+1, pos+1+len(param_modes))]
        if opcode in [1,2,7,8]:
            if param_modes[-1] == 2:
                storage_loc1278 = self.source_code[pos+3] + self.relative_base
            else:
                storage_loc1278 = self.source_code[pos+3]
        if opcode == 99:
            self.solved = True
            self.halt = True
        elif opcode == 1:
            values = self.param_values(parameters, param_modes)
            self.source_code[storage_loc1278] = values[0] + values[1]
            self.pos += 4
        elif opcode == 2:
            values = self.param_values(parameters, param_modes)
            self.source_code[storage_loc1278] = values[0] * values[1]
            self.pos += 4
        elif opcode == 3:
            if len(self.inputs) > 0:
                input = self.inputs.pop(0)
            else:
                self.halt = True
                return
            if param_modes[0] == 2:
                self.source_code[self.source_code[pos + 1] + self.relative_base] = input
            else:
                self.source_code[self.source_code[pos + 1]] = input
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
                self.source_code[storage_loc1278] = 1
            else:
                self.source_code[storage_loc1278] = 0
            self.pos += 4
        elif opcode == 8:
            values = self.param_values(parameters, param_modes)
            if values[0] == values[1]:
                self.source_code[storage_loc1278] = 1
            else:
                self.source_code[storage_loc1278] = 0
            self.pos += 4
        elif opcode == 9:
            value = self.fetch_param(parameters[0], param_modes[0])
            self.relative_base += value
            self.pos += 2

    def next(self, inputs=[]):
        self.halt = False
        self.inputs = inputs
        self.outputs = []
        while not self.halt:
            self.compute_step()
        return self.outputs, self.solved


class AmplifierChain:

    def __init__(self, control_software, phase_setting=None, n_amplifiers=5):
        self.acs = copy.deepcopy(control_software)
        self.amplifiers = []
        for x in range(n_amplifiers):
            ps = phase_setting[x]
            self.amplifiers.append(IntcodeComputer(self.acs, ps))

    def thruster_signal(self, first_input=0):
        amp_out = first_input
        i = 0
        for amp in self.amplifiers:
            outputs, _ = amp.next([amp_out])
            amp_out = outputs[-1]
            i += 1
        return amp_out

    def thruster_signal2(self, first_input=0):
        amp_out = [first_input]
        solved = False
        i = 0
        while not solved:
            amp = self.amplifiers[i % 5]
            amp_out, solved = amp.next(amp_out)
            if i % 5 != 4:
                solved = False
            i += 1
        return amp_out[-1]


class TestIntcodeComputer:

    def test_opcodes_1_2():
        A = IntcodeComputer('1,9,10,3,2,3,11,0,99,30,40,50')

        # Intcode A tests opcode 1, 2 then stops
        # Test Opcode 1
        A.compute_step()
        assert list(A.source_code.values()) == [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert A.solved == False
        # Test Opcode 2
        A.compute_step()
        assert list(A.source_code.values()) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert A.solved == False
        # Should be done now
        A.compute_step()
        assert list(A.source_code.values()) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert A.solved

        # Now using the "next" function which should iterate until it reaches
        # An input instruction with no input or a stop command.
        A = IntcodeComputer('1,9,10,3,2,3,11,0,99,30,40,50')
        assert list(A.source_code.values()) == [1,9,10,3,2,3,11,0,99,30,40,50]
        assert A.solved == False
        # Test Opcode 2
        A.next()
        assert list(A.source_code.values()) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        assert A.solved

        # Intcode B adds 1 to 1 then stops
        B = IntcodeComputer('1,0,0,0,99')
        B.compute_step()
        assert list(B.source_code.values()) == [2, 0, 0, 0, 99]
        assert B.solved == False
        B.compute_step()
        assert B.solved

        # Intcode C multiplies 3 * 2 then stops
        C = IntcodeComputer('2,3,0,3,99')
        C.compute_step()
        assert list(C.source_code.values()) == [2, 3, 0, 6, 99]
        C.compute_step()
        assert C.solved

        # Intcode D multiplies 99 * 99 then stops
        D = IntcodeComputer('2,4,4,5,99,0')
        D.compute_step()
        assert list(D.source_code.values()) == [2, 4, 4, 5, 99, 9801]
        D.compute_step()
        assert D.solved

        # Intcode E performs two operations and then stops
        E = IntcodeComputer('1,1,1,4,99,5,6,0,99')
        E = IntcodeComputer('1,1,1,4,99,5,6,0,99')
        E.compute_step()
        assert list(E.source_code.values()) == [1, 1, 1, 4, 2, 5, 6, 0, 99]
        E.compute_step()
        assert list(E.source_code.values()) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    def test_opcodes_3_4():
        # Test 3 & 4. Opcode A should output what is input and then stop.
        A = IntcodeComputer('3,0,4,0,99')
        A.inputs = [10]
        A.compute_step()
        assert list(A.source_code.values()) == [10, 0, 4, 0, 99]
        x = A.compute_step()
        assert x == 10
        A.compute_step()
        assert A.solved
        A.compute_step()
        assert A.solved

        A = IntcodeComputer('3,0,4,0,99')
        A.next([10])
        assert list(A.source_code.values()) == [10, 0, 4, 0, 99]
        assert A.outputs == [10]
        assert A.solved

        B = IntcodeComputer('1101,100,-1,4,0')
        B.compute_step()
        assert list(B.source_code.values()) == [1101, 100, -1, 4, 99]
        assert B.pos == 4
        assert B.solved == False
        B.compute_step()
        assert B.solved

        # Test Day 5 input
        C = IntcodeComputer('3,7,1,8,6,6,1100,1,238,225', 101)
        C.compute_step()
        assert list(C.source_code.values()) == [3, 7, 1, 8, 6, 6, 1338, 101, 238, 225]
        C = IntcodeComputer(read_input('day05.txt')[0], 1)
        C.next()
        assert C.output == 14155342

    def test_opcodes_5_6():
        # Test Opcodes 5 & 6

        # Both tests output 0 if input is 0 (either from next or phase setting) and 1 otherwise
        E = IntcodeComputer('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
        outputs, solved = E.next([0])
        assert outputs == [0]
        E = IntcodeComputer('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
        outputs, solved = E.next([100])
        assert outputs == [1]

        F = IntcodeComputer('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 0)
        outputs, solved = F.next([1])
        assert outputs == [0]
        F = IntcodeComputer('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 16)
        outputs, solved = F.next([0])
        assert outputs == [1]

        x = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
        G = IntcodeComputer(x)
        outputs, solved = G.next([100])
        assert outputs == [1001]
        G = IntcodeComputer(x)
        outputs, solved = G.next([-6])
        assert outputs == [999]
        G = IntcodeComputer(x)
        outputs, solved = G.next([8])
        assert outputs == [1000]

    def test_opcodes_7_8():
        # If input is equal to 8 return 1 else 0
        A = IntcodeComputer('3,9,8,9,10,9,4,9,99,-1,8', 5)
        outputs, solved = A.next()
        assert outputs == [0]
        assert solved
        A = IntcodeComputer('3,9,8,9,10,9,4,9,99,-1,8', 8)
        outputs, solved = A.next()
        assert outputs == [1]
        assert solved

        # If input is less than 8 return 1 else 0
        B = IntcodeComputer('3,9,7,9,10,9,4,9,99,-1,8', 10)
        outputs, solved = B.next()
        assert outputs == [0]
        assert solved
        B = IntcodeComputer('3,9,7,9,10,9,4,9,99,-1,8', 6)
        outputs, solved = B.next()
        assert outputs == [1]
        assert solved

        # If input is equal to 8 return 1 else 0
        C = IntcodeComputer('3,3,1108,-1,8,3,4,3,99', 100)
        outputs, solved = C.next()
        assert outputs == [0]
        assert solved
        C = IntcodeComputer('3,3,1108,-1,8,3,4,3,99', 8)
        outputs, solved = C.next()
        assert outputs == [1]
        assert solved

        # If input is less than 8 return 1 else 0
        D = IntcodeComputer('3,9,7,9,10,9,4,9,99,-1,8', 8)
        outputs, solved = D.next()
        assert outputs == [0]
        assert solved
        D = IntcodeComputer('3,9,7,9,10,9,4,9,99,-1,8', 0)
        outputs, solved = D.next()
        assert outputs == [1]
        assert solved

    def test_amplifier_chain():
        txt = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        ac0 = AmplifierChain(txt, [4, 3, 2, 1, 0])
        assert ac0.thruster_signal(0) == 43210

        txt = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
        ac1 = AmplifierChain(txt, [0, 1, 2, 4, 3])
        assert ac1.thruster_signal(0) == 54312

        txt = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
        ac3 = AmplifierChain(txt, [1, 0, 4, 3, 2])
        assert ac3.thruster_signal(0) == 65210

        # Day 7 part 1 solution
        ac4 = AmplifierChain(read_input('day07.txt')[0], [2,3,0,4,1])
        assert ac4.thruster_signal(0) == 24405


        txt = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
        ac5 = AmplifierChain(txt, [9, 8, 7, 6, 5])
        assert ac5.thruster_signal2(0) == 139629729

        txt = '''
        3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
        -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
        53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
        '''
        ac6 = AmplifierChain(txt, [9, 7, 8, 5, 6])
        assert ac6.thruster_signal2(0) == 18216

    def test_relative_mode():

        A = IntcodeComputer('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
        assert A.next()[0] == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

        B = IntcodeComputer('1102,34915192,34915192,7,4,7,99,0')
        assert B.next()[0][0] == 1219070632396864

        C = IntcodeComputer('109,1,203,11,109,1,204,10,99')
        C.next([16])
        assert C.output == 16

        D = IntcodeComputer('109,1,203,11,209,8,204,1,99,10,0,42,0')
        D.next([16])
        assert D.output == 16

        E = IntcodeComputer('109,1,21108,1,0,7,99,0,1')
        E.next([12])
        assert E.source_code[8] == 0
        E = IntcodeComputer('109,1,21108,1,1,7,99,0,0')
        E.next([12])
        assert E.source_code[8] == 1

        F = IntcodeComputer('104,1125899906842624,99')
        F.next([0])
        assert F.output == 1125899906842624


if __name__ == '__main__':
    import pdb

    TestIntcodeComputer.test_opcodes_1_2()
    TestIntcodeComputer.test_opcodes_3_4()
    TestIntcodeComputer.test_opcodes_5_6()
    TestIntcodeComputer.test_opcodes_7_8()
    TestIntcodeComputer.test_amplifier_chain()
    TestIntcodeComputer.test_relative_mode()
