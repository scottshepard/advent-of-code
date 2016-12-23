import re

class Register:

    def __init__(self, name):
        self.name = name
        self.value = 0

    def __str__(self):
        return str({self.name: self.value})

    def cpy(self, value):
        self.value = value

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

class InstructionParser:

    def __init__(self, instructions):
        self.instructions = instructions
        self.next_instruction_i = 0
        self.registers = [Register(x) for x in list('abcd')]

    def __repr__(self):
        return str([str(x) for x in self.registers])

    def tgl(self, register):

    def parse_instructions(self, up_to):
        index = 0
        move = 0
        while index < up_to:
            if move % 500000 == 0:
                print('Move:', move, self, end='\r')
            instruction = self.instructions[index]
            index += self.parse_instruction(instruction)
            move += 1

    def parse_instruction(self, instruction):
        method = re.search('cpy|inc|dec|jnz|tgl', instruction).group(0)
        if method == 'tgl':
        elif method == 'cpy':
            letter = re.search('[a-z]$', instruction).group(0)
            register = self.register(letter)
            value = re.search('-?[0-9]+|((?<= )[a-z](?= ))', instruction).group(0)
            if value in list('abcd'):
                register.cpy(self.register(value).value)
            else:
                register.cpy(int(value))
            increment = 1
        elif method == 'inc':
            letter = re.search('[a-z]$', instruction).group(0)
            register = self.register(letter)
            register.inc()
            increment = 1
        elif method == 'dec':
            letter = re.search('[a-z]$', instruction).group(0)
            register = self.register(letter)
            register.dec()
            increment = 1
        elif method == 'jnz':
            letter = re.search('(?<=jnz )([a-z]|(-?[0-9]))', instruction).group(0)
            if letter in list('abcd'):
                value = self.register(letter).value
            else:
                value = int(letter)
            increment = int(re.search('-?[0-9]+$', instruction).group(0))
            if value == 0:
                increment = 1
        return increment

    def register(self, name):
        return [r for r in self.registers if r.name == name][0]

if __name__ == '__main__':
    lines = open('inputs/day23.txt').read().splitlines()
