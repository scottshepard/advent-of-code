# --- Day 12: Leonardo's Monorail ---
#
# You finally reach the top floor of this building: a garden with a slanted 
# glass ceiling. Looks like there are no more stars to be had.
#
# While sitting on a nearby bench amidst some tiger lilies, you manage to 
# decrypt some of the files you extracted from the servers downstairs.
#
# According to these documents, Easter Bunny HQ isn't just this building - 
# it's a collection of buildings in the nearby area. They're all connected 
# by a local monorail, and there's another building not far from here! 
# Unfortunately, being night, the monorail is currently not operating.
#
# You remotely connect to the monorail control systems and discover that the 
# boot sequence expects a password. The password-checking logic 
# (your puzzle input) is easy to extract, but the code it uses is strange: 
# it's assembunny code designed for the new computer you just assembled. 
# You'll have to execute the code and get the password.
#
# The assembunny code you've extracted operates on four registers 
# (a, b, c, and d) that start at 0 and can hold any integer. 
# However, it seems to make use of only a few instructions:
#
# cpy x y copies x (either an integer or the value of a register) into 
# register y.
# inc x increases the value of register x by one.
# dec x decreases the value of register x by one.
# jnz x y jumps to an instruction y away (positive means forward; 
# negative means backward), but only if x is not zero.
# The jnz instruction moves relative to itself: an offset of -1 would 
# continue at the previous instruction, while an offset of 2 would skip over 
# the next instruction.
#
# For example:
#
# cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a
#
# The above code would set register a to 41, increase its value by 2, decrease its value by 1, and then skip the last dec a (because a is not zero, so the jnz a 2 skips it), leaving register a at 42. When you move past the last instruction, the program halts.
#
# After executing the assembunny code in your puzzle input, what value is left in register a?
#
# -----------------------------------------------------------------------------

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

    def parse_instructions(self, up_to):
        index = 0
        while index < up_to - 1:
            print(index)
            instruction = self.instructions[index]
            index += self.parse_instruction(instruction)
        return self

    def parse_instruction(self, instruction):
        method = re.search('cpy|inc|dec|jnz', instruction).group(0)
        if method == 'cpy':
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
            increment = int(re.search('-?[0-9]+', instruction).group(0))
            if value == 0:
                increment = 1
        print(instruction)
        print(self)
        return increment

    def register(self, name):
        return [r for r in self.registers if r.name == name][0]

if __name__ == '__main__':
    instructions = open('inputs/day12.txt').read().splitlines()
    ip = InstructionParser(instructions)
    # ip.parse_instructions(22)
    




