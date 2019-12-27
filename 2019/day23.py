from copy import deepcopy
from utils import read_input
from intcode import IntcodeComputer

input = read_input('day23.txt')[0]

class Network:

    def __init__(self, input):
        self.input = deepycopy(input)
        self.network = [IntcodeComputer(input, i) for i in range(50)]
        self.packets = []
