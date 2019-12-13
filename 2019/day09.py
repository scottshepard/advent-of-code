
from utils import read_input
from intcode import IntcodeComputer

input = read_input('day09.txt')[0]
ic = IntcodeComputer(input)
ic.next([1])
print(ic.outputs)
