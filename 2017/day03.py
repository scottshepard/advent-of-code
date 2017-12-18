# --- Day 3: Spiral Memory ---
#
# You come across an experimental new kind of memory stored on an infinite 
# two-dimensional grid.
#
# Each square on the grid is allocated in a spiral pattern starting at a 
# location marked 1 and then counting up while spiraling outward. 
# For example, the first few squares are allocated like this:

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
#
# While this is very space-efficient (no squares are skipped), requested data 
# must be carried back to square 1 (the location of the only access port for 
# this memory system) by programs that can only move up, down, left, or right. 
# They always take the shortest path: the Manhattan Distance between the 
# location of the data and square 1.
#
# For example:
#
# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.
# How many steps are required to carry the data from the square identified in 
# your puzzle input all the way to the access port?
#
# Your puzzle input is 325489.
# Answer: 552
#
# --- Part Two ---
#
# As a stress test on the system, the programs here clear the grid and then 
# store the value 1 in square 1. Then, in the same allocation order as shown 
# above, they store the sum of the values in all adjacent squares, including 
# diagonals.
#
# So, the first few squares' values are chosen as follows:
#
# Square 1 starts with the value 1.
# Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
# Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
# Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
# Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
# Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:
#
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
#
# What is the first value written that is larger than your puzzle input?
#
# Your puzzle input is still 325489.
#
# ------------------------------------------------------------------------------

import math
import re
import os
from sys import argv

def solve1(input):
    coords = coordinates(input)
    dist = manhattan_dist(coords[0], coords[1])
    return dist

def manhattan_dist(start, end):
    return abs(start) + abs(end)

def coordinates(n):
    ps = next_odd_perfect_square(n)
    level = len(odds(n))-1
    sidelen = math.sqrt(ps)-1
    coords = [level, -level]
    iterator = ps
    while iterator > n:
        if iterator > ps - (sidelen):
            coords[0] -= 1
        elif iterator > ps - sidelen*2:
            coords[1] += 1
        elif iterator > ps - 3*(sidelen):
            coords[0] += 1
        elif iterator > ps - 4*(sidelen):
            coords[1] -= 1
        iterator -= 1
    return coords

def next_odd_perfect_square(n):
    perfect_squares = [x ** 2 for x in odds(n)]
    return [x for x in perfect_squares if x >= n][0]

def odds(n):
    arr = [1]
    sqrt = math.sqrt(n)
    while sqrt > arr[-1]:
        arr.append(arr[-1]+2)
    return arr

class Spiral:

    def __init__(self, n):
        self.squares = {}
        self.n = n
        self.add_square(0, 0, 1)

    def add_square(self, x, y, n):
        self.squares[(x, y)] = n
        
    def calculate_next_square(self, coords):
        adjacent_coords = [
          (coords[0] + 1, coords[1]),
          (coords[0] + 1, coords[1] + 1),
          (coords[0], coords[1] + 1),
          (coords[0] - 1, coords[1] + 1),
          (coords[0] - 1, coords[1]),
          (coords[0] - 1, coords[1] - 1),
          (coords[0], coords[1] - 1),
          (coords[0] + 1, coords[1] - 1)
        ]
        total = 0
        for coord in adjacent_coords:
            try:
                total += self.squares[coord]
            except: 
                pass
        return total

    def build_next_square(self):
        coords = coordinates(len(self.squares)+1)
        self.add_square(coords[0], coords[1], self.calculate_next_square(coords))

    def solve(self):
        while self.squares[list(self.squares.keys())[-1]] <= self.n:
            self.build_next_square()
        return self.squares[list(self.squares.keys())[-1]]
        
        

if __name__ == '__main__':
    if (len(argv) == 1):
        input = 325489
    else:
        input = int(argv[1])
    print(solve1(input))
    spiral = Spiral(input)
    print(spiral.solve())
