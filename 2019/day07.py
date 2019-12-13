import copy
from utils import read_input
from itertools import permutations
import pandas as pd
import pdb

from intcode import IntcodeComputer, AmplifierChain

def find_max_thruster_signal(input_code, signal_digits=[0,1,2,3,4]):
    thruster_signals = []
    perms = permutations(signal_digits)
    for perm in list(perms):
        ac = AmplifierChain(input_code, perm)
        thruster_signals.append(ac.thruster_signal(0))
    return pd.Series(thruster_signals).max()


if __name__ == '__main__':
    # For real now
    acs = read_input('day07.txt')[0]
    print('Solution to Day 7 Part I is {}'.format(find_max_thruster_signal(acs)))

    # Part 2
    #acs_test2 = aoc.read_input('day07_test2.txt')
    #ac2 = AmplifierChain(acs_test2[0], phase_setting=[9,8,7,6,5])
    #ac2.thruster_signal2(0)
