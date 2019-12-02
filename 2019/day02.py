import advent_of_code as aoc


def format_input(input_):
    return [int(i) for i in input_.split(',')]


class Intcode:

    def __init__(self, opcode):
        self.opcode = opcode
        self.pos = 0
        self.solved = False

    def revert_to_1202(self):
        self.opcode[1] = 12
        self.opcode[2] = 2

    def compute_step(self):
        opcode = self.opcode
        pos = self.pos
        val = opcode[pos]
        if val == 99:
            self.solved = True
            return
        elif val == 1:
            opcode[opcode[pos+3]] = opcode[opcode[pos+1]] + opcode[opcode[pos+2]]
        elif val == 2:
            opcode[opcode[pos+3]] = opcode[opcode[pos+1]] * opcode[opcode[pos+2]]
        self.pos += 4
        self.opcode = opcode

    def solve1(self):
        while not self.solved:
            self.compute_step()
        return self.opcode[0]

if __name__ == '__main__':
    test_inputs = aoc.read_input('day02_test.txt')
    test_inputs = [format_input(i) for i in test_inputs]
    for ti in test_inputs:
        intcode = Intcode(ti)
        print('Test input {0} solution is {1}'.format(ti, intcode.solve1()))

    input = format_input(aoc.read_input('day02.txt')[0])
    intcode = Intcode(input)
    intcode.revert_to_1202()
    print('Step 1 solution is {}'.format(intcode.solve1()))

