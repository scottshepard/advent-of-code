# --- Day 23: Safe Cracking ---
#
# This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's
# private office is here, complete with a safe hidden behind a painting, 
# and who wouldn't hide a star in a safe behind a painting?
#
# The safe has a digital screen and keypad for code entry. A sticky note 
# attached to the safe has a password hint on it: "eggs". The painting is of a 
# large rabbit coloring some eggs. You see 7.
#
# When you go to type the code, though, nothing appears on the display; 
# instead, the keypad comes apart in your hands, apparently having been 
# smashed. Behind it is some kind of socket - one that matches a connector in 
# your prototype computer! You pull apart the smashed keypad and extract the 
# logic circuit, plug it into your computer, and plug your computer into the 
# safe.
#
# Now, you just need to figure out what output the keypad would have sent to 
# the safe. You extract the assembunny code from the logic chip 
# (your puzzle input).
#
# The code looks like it uses almost the same architecture and instruction set 
# that the monorail computer used! You should be able to use the same 
# assembunny interpreter for this as you did there but with one new instruction
#
# tgl x toggles the instruction x away (pointing at instructions like jnz does:
# positive means forward; negative means backward):
#
# For one-argument instructions, inc becomes dec, and all other one-argument 
# instructions become inc.
# For two-argument instructions, jnz becomes cpy, and all other 
# two-instructions become jnz.
# The arguments of a toggled instruction are not affected.
# If an attempt is made to toggle an instruction outside the program, nothing 
# happens.
# If toggling produces an invalid instruction (like cpy 1 2) and an attempt is 
# later made to execute that instruction, skip it instead.
# If tgl toggles itself (for example, if a is 0, tgl a would target itself and 
# become inc a), the resulting instruction is not executed until the next time 
# it is reached.
#
# For example, given this program:
#
# cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a
#
# cpy 2 a initializes register a to 2.
# The first tgl a toggles an instruction a (2) away from it, which changes the 
# third tgl a into inc a.
# The second tgl a also modifies an instruction 2 away from it, which changes 
# the cpy 1 a into jnz 1 a.
# The fourth line, which is now inc a, increments a to 3.
# Finally, the fifth line, which is now jnz 1 a, jumps a (3) instructions 
# ahead, skipping the dec a instructions.
# In this example, the final value in register a is 3.
#
# The rest of the electronics seem to place the keypad entry (the number of 
# eggs, 7) in register a, run the code, and then send the value left in 
# register a to the safe.
#
# What value should be sent to the safe?
#
# ----------------------------------------------------------------------------

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
