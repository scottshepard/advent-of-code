import advent_of_code as aoc
import copy


def format_input(input_):
    return [int(i) for i in input_.split(',')]


class Intcode:

    def __init__(self, opcode):
        self.opcode_raw = opcode
        self.opcode = copy.deepcopy(opcode)
        self.pos = 0
        self.solved = False

    def reset(self):
        self.opcode = copy.deepcopy(self.opcode_raw)
        self.solved = False
        self.pos = 0

    def adjust_input(self, noun_, verb_):
        self.opcode[1] = noun_
        self.opcode[2] = verb_

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

    def solve2(self, target):
        self.target = target
        self.verb = self.find_verb(0)
        self.noun = self.find_noun(0)
        return 100 * self.noun + self.verb

    def find_verb(self, verb_guess):
        self.reset()
        self.adjust_input(0, verb_guess)
        guess = self.solve1()
        if int(str(guess)[-2:]) == int(str(self.target)[-2:]):
            return verb_guess
        elif int(str(guess)[-2:]) > int(str(self.target)[-2:]):
            return self.find_verb(verb_guess-1)
        elif int(str(guess)[-2:]) < int(str(self.target)[-2:]):
            return self.find_verb(verb_guess + 1)

    def find_noun(self, noun_guess):
        self.reset()
        self.adjust_input(noun_guess, self.verb)
        guess = self.solve1()
        if guess == self.target:
            return noun_guess
        elif guess > self.target:
            return self.find_noun(noun_guess-1)
        elif guess < self.target:
            return self.find_noun(noun_guess+1)


if __name__ == '__main__':
    test_inputs = aoc.read_input('day02_test.txt')
    test_inputs = [format_input(i) for i in test_inputs]
    for ti in test_inputs:
        intcode = Intcode(ti)
        print('Test input {0} solution is {1}'.format(ti, intcode.solve1()))

    input = format_input(aoc.read_input('day02.txt')[0])
    intcode = Intcode(input)
    intcode.adjust_input(12, 2)
    print('Step 1 solution is {}'.format(intcode.solve1()))
    print('Step 2 solution in {}'.format(intcode.solve2(19690720)))
