# --- Day 25: Clock Signal ---
#
# You open the door and find yourself on the roof. The city sprawls away from 
# you for miles and miles.
#
# There's not much time now - it's already Christmas, but you're nowhere near
# the North Pole, much too far to deliver these stars to the sleigh in time.
#
# However, maybe the huge antenna up here can offer a solution. After all, the
# sleigh doesn't need the stars, exactly; it needs the timing data they provide
# and you happen to have a massive signal generator right here.
#
# You connect the stars you have to your prototype computer, connect that to 
# the antenna, and begin the transmission.
#
# Nothing happens.
#
# You call the service number printed on the side of the antenna and quickly 
# explain the situation. "I'm not sure what kind of equipment you have 
# connected over there," he says, "but you need a clock signal." You try to 
# explain that this is a signal for a clock.
#
# "No, no, a clock signal - timing information so the antenna computer knows 
# how to read the data you're sending it. An endless, alternating pattern of 
# 0, 1, 0, 1, 0, 1, 0, 1, 0, 1...." He trails off.
#
# You ask if the antenna can handle a clock signal at the frequency you would 
# need to use for the data from the stars. "There's no way it can! The only 
# antenna we've installed capable of that is on top of a top-secret Easter 
# Bunny installation, and you're definitely not-" You hang up the phone.
#
# You've extracted the antenna's clock signal generation assembunny code 
# (your puzzle input); it looks mostly compatible with code you worked on just 
# recently.
#
# This antenna code, being a signal generator, uses one extra instruction:
#
# out x transmits x (either an integer or the value of a register) as the next 
# value for the clock signal.
# The code takes a value (via register a) that describes the signal to generate
# but you're not sure how it's used. You'll have to find the input to produce 
# the right signal through experimentation.
#
# What is the lowest positive integer that can be used to initialize register a
# and cause the code to output a signal of 0, 1, 0, 1... repeating forever?
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
        if self.index == 2:
            b = self.register('b')
            c = self.register('c')
            d = self.register('d')
            d.inc(633 * c.value)
            c.cpy(0)
            b.cpy(0)
            self.index = 8
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

    def out(self, instruction):
        letter = re.search('[a-z]$', instruction).group(0)
        register = self.register(letter)
        print(register.value)
        self.index += 1

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
    interp.register('a').cpy(0)
