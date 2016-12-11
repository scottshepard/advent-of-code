# --- Day 18: Like a GIF For Your Yard ---
#
# After the million lights incident, the fire code has gotten stricter: now, at
# most ten thousand lights are allowed. You arrange them in a 100x100 grid.
#
# Never one to let you down, Santa again mails you instructions on the ideal 
# lighting configuration. With so few lights, he says, you'll have to resort to
# animation.
#
# Start by setting your lights to the included initial configuration 
# (your puzzle input). A # means "on", and a . means "off".
#
# Then, animate your grid in steps, where each step decides the next 
# configuration based on the current one. Each light's next state
# (either on or off) depends on its current state and the current states of the
# eight lights adjacent to it (including diagonals). Lights on the edge of the 
# grid might have fewer than eight neighbors; the missing ones always count as 
# "off".
#
# For example, in a simplified 6x6 grid, the light marked A has the neighbors 
# numbered 1 through 8, and the light marked B, which is on an edge, only has 
# the neighbors marked 1 through 5:
#
# 1B5...
# 234...
# ......
# ..123.
# ..8A4.
# ..765.
# 
# The state a light should have next is based on its current state (on or off) 
# plus the number of neighbors that are on:
#
# A light which is on stays on when 2 or 3 neighbors are on, 
# and turns off otherwise.
# A light which is off turns on if exactly 3 neighbors are on,
# and stays off otherwise.
# All of the lights update simultaneously; they all consider the same current 
# state before moving to the next.
#
# Here's a few steps from an example configuration of another 6x6 grid:
#
# Initial state:
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..
#
# After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# #.....
# #.##..
#
# After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....
#
# After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......
#
# After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......
# After 4 steps, this example has four lights on.
#
# In your grid of 100x100 lights, given your initial configuration, 
# how many lights are on after 100 steps?
#
# ----------------------------------------------------------------------------

import re

class Light:

    def __init__(self, x, y, char, anchor = False):
        self.x = x
        self.y = y
        self.char = char
        self.on = self.on(char)
        self.next_state = self.on
        self.anchor = anchor

    def __repr__(self):
        return self.char

    def on(self, char):
        if char == '#':
            return True
        else:
            return False

    def set_next_state(self, sum_neighbors):
        if self.anchor:
            print('Here')
            self.next_state = self.on
        else:
            if self.on:
                if sum_neighbors in [2, 3]:
                    self.next_state = True
                else:
                     self.next_state = False
            else:
                if sum_neighbors == 3:
                     self.next_state = True
                else:
                     self.next_state = False

    def update_next_state(self):
        self.on = self.next_state
        self.update_char(self.on)

    def update_char(self, bool_):
        if bool_:
            self.char = '#'
        else:
            self.char = '.'

class Grid:

    def __init__(self, n_cols, n_rows, anchor_corners = True):
        self.grid = [['' for x in range(n_cols)] for y in range(n_rows)]
        self.n_rows = n_rows
        self.n_cols = n_cols

    def __repr__(self):
        grid = self.grid
        return ''.join([''.join([l.char for l in row]) + '\n' for row in grid])

    def __getitem__(self, i):
        return self.grid[i]

    def sum_lights(self):
        return sum([sum([l.on for l in row]) for row in self.grid])

    def add_light(self, x, y, char):
        if self.is_corner(x, y):
            self.grid[y][x] = Light(x, y, char, True)
        else:
            self.grid[y][x] = Light(x, y, char)

    def is_corner(self, x, y):
        n_cols = self.n_cols
        n_rows = self.n_rows
        corners = [(0, 0), (n_cols-1, 0), (0, n_rows-1), (n_cols-1, n_rows-1)]
        return (x, y) in corners

    def get_light(self, x, y):
        if x == -1 or y == -1:
            return
        try:
            return self.grid[y][x]
        except:
            pass

    def sum_neighbors(self, x, y):
        return sum([x.on for x in self.get_neighbors(x, y)])

    def get_neighbors(self, x, y):
        grid = self.grid
        light = self.get_light(x, y)
        neighbors = []
        for j in range(y-1, y+2):
            for i in range(x-1, x+2):
                if (i, j) != (x, y):
                    neighbors.append(self.get_light(i, j))
        return [n for n in neighbors if n is not None]

    def step(self):
        for row in self.grid:
            for light in row:
                light.set_next_state(self.sum_neighbors(light.x, light.y))
        for row in self.grid:
            for light in row:
                light.update_next_state()
        return self

class Day18:

    def __init__(self, data):
        self.lines = re.split('\n', data)
        self.grid = Grid(len(self.lines[0]), len(self.lines))
        for j in range(self.grid.n_rows):
            for i in range(self.grid.n_cols):
                self.grid.add_light(i, j, self.lines[j][i])

    def run_part_1(self):
        for i in range(100):
            self.grid.step()
        return self.grid.sum_lights()

if __name__ == '__main__':
    data = open('day18_test2.txt').read()
    lines = re.split('\n', data)
    day18 = Day18(data)
    # print('Part 1:', day18.run_part_1())
    grid = day18.grid
