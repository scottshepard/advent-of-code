from utils import read_input
import numpy as np


input = read_input('day03.txt')



def count_trees_on_slope(slope, mountain):
    x = 0
    y = 0
    h = len(mountain)
    w = len(mountain[0])
    trees = 0
    while y < h-1:
        x = (x + slope['x']) % w
        y += slope['y']
        trees += int(mountain[y][x] == '#')
    return trees

slope_part_1 = {'x':3, 'y':1}

print('Part 1: ', count_trees_on_slope(slope_part_1, input))

slopes_part_2 = [
    {'x':1, 'y':1},
    {'x':3, 'y':1},
    {'x':5, 'y':1},
    {'x':7, 'y':1},
    {'x':1, 'y':2}
]
trees_list = [count_trees_on_slope(s, input) for s in slopes_part_2]
print('Part 2:', np.prod(trees_list))
