# --- Day 8: I Heard You Like Registers ---
#
# You receive a signal directly from the CPU. Because of your recent assistance
# with jump instructions, it would like you to compute the result of a series
# of unusual register instructions.
#
# Each instruction consists of several parts: the register to modify,
# whether to increase or decrease that register's value, the amount by which to
# increase or decrease it, and a condition. If the condition fails, skip the
# instruction without modifying the register. The registers all start at 0.
# The instructions look like this:
#
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
#
# These instructions would be processed as follows:
#
# Because a starts at 0, it is not greater than 1, and so b is not modified.
# a is increased by 1 (to 1) because b is less than 5 (it is 0).
# c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
# c is increased by -20 (to -10) because c is equal to 10.
# After this process, the largest value in any register is 1.
#
# You might also encounter <= (less than or equal to) or != (not equal to).
# However, the CPU doesn't have the bandwidth to tell you what all the
# registers are named, and leaves that to you to determine.
#
# What is the largest value in any register after completing the instructions
# in your puzzle input?
#
# ------------------------------------------------------------------------------

import os
import re

class CPU:

    def __init__(self, lines):
        self.lines = lines
        self.index = 0
        self.registers = {}
        self.max = 0

    def __iter__(self):
        return self

    def next(self):
        if self.index < len(self.lines):
            self.index += 1
            return self.lines[self.index-1]
        else:
            raise StopIteration

    def parse_line(self, line):
        pieces = line.split(' ')
        reg = pieces[0]
        creg = pieces[4]
        # If the registers don't exit yet set them to 0
        if reg not in list(self.registers.keys()):
            self.registers[reg] = 0
        if creg not in list(self.registers.keys()):
            self.registers[creg] = 0
        # Check register against current max value and store if greater
        if self.registers[reg] > self.max:
            self.max = self.registers[reg]
        inst = pieces[1]
        val = int(pieces[2])
        # Add the variable value into memory so that the condition can be 
        # evaluated stright from a string
        exec "%s=%s" % (creg, self.registers[pieces[4]])
        condition = pieces[4] + pieces[5] + pieces[6]
        if eval(condition):
            if inst == 'inc':
                self.registers[reg] += val
            elif inst == 'dec':
                self.registers[reg] -= val

    def solve(self):
        for line in self:
            self.parse_line(line)
        return max(list(self.registers.values())), self.max

if __name__ == '__main__':    
    rel_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(rel_path, "inputs/day08.txt")
    f = open(file_path)
    data = f.read().split('\n')
    cpu = CPU(data)
    print(cpu.solve())
