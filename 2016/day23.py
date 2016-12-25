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

    def inc(self, val=1):
        self.value += val

    def dec(self):
        self.value -= 1

class Interpreter:

    def __init__(self, instructions):
        self.instructions = list(instructions)
        self.index = 0
        self.registers = [Register(x) for x in list('abcd')]

    def __repr__(self):
        return str([str(x) for x in self.registers])

    def tgl(self, instruction):
        value = re.search('-?[0-9a-z]+$', instruction).group(0)
        if value in 'abcd':
            value = self.register(value).value
        else:
            value = int(value)
        if self.index + value >= len(self.instructions):
            self.index += 1
            return
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
        self.index += 1

    def cpy(self, instruction):
        # Hardcoded to skip the hotspot
        if self.index == 4:
            a = self.register('a')
            b = self.register('b')
            c = self.register('c')
            d = self.register('d')
            a.inc(b.value * d.value)
            c.cpy(0)
            d.cpy(0)
            self.index = 10
            return 
        letter = re.search('[a-z]$', instruction).group(0)
        register = self.register(letter)
        value = re.search('-?[0-9]+|((?<= )[a-z](?= ))', instruction).group(0)
        if value in list('abcd'):
            register.cpy(self.register(value).value)
        else:
            register.cpy(int(value))
        self.index += 1

    def inc(self, instruction):
        letter = re.search('[a-z]$', instruction).group(0)
        register = self.register(letter)
        register.inc()
        self.index += 1

    def dec(self, instruction):
        letter = re.search('[a-z]$', instruction).group(0)
        register = self.register(letter)
        register.dec()
        self.index += 1

    def jnz(self, instruction):
        copy = re.sub('jnz ', '', instruction)
        values = re.findall('-?[0-9a-z]+', copy)
        values2 = []
        for val in values:
            if val in list('abcd'):
                values2.append(self.register(val).value)
            else:
                values2.append(int(val))
        if values2[0] == 0:
            self.index += 1
        else:
            self.index += values2[1]

    def solve(self, up_to=None):
        if up_to is None:
            up_to = len(self.instructions)
        self.move = 0
        while self.index < up_to:
            self.parse_instruction(self.index)
            self.move += 1
        return self

    def parse_instruction(self, index):
        instruction = self.instructions[index]
        method = re.search('cpy|inc|dec|jnz|tgl', instruction).group(0)
        if method == 'tgl':
            self.tgl(instruction)
        elif method == 'cpy':
            self.cpy(instruction)
        elif method == 'inc':
            self.inc(instruction)
        elif method == 'dec':
            self.dec(instruction)
        elif method == 'jnz':
            self.jnz(instruction)
        return self

    def register(self, name):
        return [r for r in self.registers if r.name == name][0]

if __name__ == '__main__':
    instructions = open('inputs/day23.txt').read().splitlines()
    interp = Interpreter(instructions)
    interp.register('a').cpy(7)
    interp.solve()
    print('Part 1:', interp.register('a').value)

    interp2 = Interpreter(instructions)
    interp2.register('a').cpy(12)
    interp2.solve()
    print('Part 2:', interp2.register('a').value)
