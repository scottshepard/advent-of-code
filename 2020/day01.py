from math import floor
import numpy as np
from utils import read_input


input = read_input('day01.txt')


def sum_to(num, lst):
    '''
    :param num: Number to sum to
    :param lst: List of ints
    :return: Two elements in the lst that sum to the num
    '''
    lst = [int(x) for x in lst]
    for i in range(len(lst)):
        for j in range(len(lst)-i):
            if lst[i] + lst[j] == num:
                return lst[i], lst[j]

x, y = sum_to(2020, input)
print('Part 1:', x * y)
