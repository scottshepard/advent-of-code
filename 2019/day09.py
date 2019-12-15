from utils import read_input
from intcode import IntcodeComputer

input = read_input('day09.txt')[0]
ic = IntcodeComputer(input)
ic.next([1])
print('Solution to Day 9 Part I is {}'.format(ic.outputs[-1]))

ic = IntcodeComputer(input)
ic.next([2])
print('Solution to Day 9 Part II is {}'.format(ic.outputs[-1]))
