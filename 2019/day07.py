from itertools import permutations
import pandas as pd
from utils import read_input
from intcode import IntcodeComputer, AmplifierChain


def find_max_thruster_signal(input_code, signal_digits=[0,1,2,3,4], part=1):
    thruster_signals = []
    perms = permutations(signal_digits)
    for perm in list(perms):
        ac = AmplifierChain(input_code, perm)
        if part == 1:
            thruster_signals.append(ac.thruster_signal(0))
        elif part == 2:
            thruster_signals.append(ac.thruster_signal2(0))
    return pd.Series(thruster_signals).max()


if __name__ == '__main__':
    # For real now
    acs = read_input('day07.txt')[0]
    print('Solution to Day 7 Part I is {}'.format(find_max_thruster_signal(acs)))

    # Part 2
    print('Solution to Day 7 Part II is {}'.format(find_max_thruster_signal(acs, [5,6,7,8,9], 2)))
