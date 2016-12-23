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

class Interpreter:

    def __init__(self, instructions):
        self.instructions = instructions
        self.next_instruction_i = 0
        self.registers = [Register(x) for x in list('abcd')]

    def __repr__(self):
        return str([str(x) for x in self.registers])

    def tgl(self, instruction):
        value = re.search('-?[0-9a-z]+$', instruction).group(0)
        if value in 'abcd':
            value = self.register(value).value
        else:
            value = int(value)
        instruction2 = self.instructions[self.index+value]
        method = re.search('cpy|inc|dec|jnz|tgl', instruction2).group(0)
        if method == 'inc':
            instruction2 = re.sub('inc', 'dec', instruction2)
        elif method in ['dec', 'tgl']:
            instruction2 = re.sub('tgl|dec', 'inc', instruction2)
        elif method == 'jnz':
            instruction2 = re.sub('jnz', 'cpy', instruction2)
        elif method == 'cpy':
            instruction2 = re.sub('cpy', 'jnz', instruction2)
        self.instructions[self.index + value] = instruction2
        return 1

    def cpy(self, instruction):
        letter = re.search('[a-z]$', instruction).group(0)
        register = self.register(letter)
        value = re.search('-?[0-9]+|((?<= )[a-z](?= ))', instruction).group(0)
        if value in list('abcd'):
            register.cpy(self.register(value).value)
        else:
            register.cpy(int(value))
        return 1

    def inc(self, instruction):
        letter = re.search('[a-z]$', instruction).group(0)
        register = self.register(letter)
        register.inc()
        return 1

    def dec(self, instruction):
        letter = re.search('[a-z]$', instruction).group(0)
        register = self.register(letter)
        register.dec()
        return 1

    def jnz(self, instruction):
        letter = re.search('(?<=jnz )([a-z]|(-?[0-9]))', instruction).group(0)
        if letter in list('abcd'):
            value = self.register(letter).value
        else:
            value = int(letter)
        increment = int(re.search('-?[0-9]+$', instruction).group(0))
        if value == 0:
            increment = 1
        return increment

    def solve(self, up_to=None, print_ = False):
        if up_to is None:
            up_to = len(self.instructions)
        self.index = 0
        self.move = 0
        while self.index < up_to:
            if print_:
                print('Move:', self.move, self, end='\n')
            instruction = self.instructions[self.index]
            self.index += self.parse_instruction(instruction)
            self.move += 1

    def parse_instruction(self, instruction):
        method = re.search('cpy|inc|dec|jnz|tgl', instruction).group(0)
        if method == 'tgl':
            return self.tgl(instruction)
        elif method == 'cpy':
            return self.cpy(instruction)
        elif method == 'inc':
            return self.inc(instruction)
        elif method == 'dec':
            return self.dec(instruction)
        elif method == 'jnz':
            return self.jnz(instruction)

    def register(self, name):
        return [r for r in self.registers if r.name == name][0]

if __name__ == '__main__':
    instructions = open('inputs/day23_test.txt').read().splitlines()
    interp = Interpreter(instructions)
