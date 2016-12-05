# --- Day 2: Bathroom Security ---
#
# You arrive at Easter Bunny Headquarters under cover of darkness. 
# However, you left in such a rush that you forgot to use the bathroom! 
# Fancy office buildings like this one usually have keypad locks on 
# their bathrooms, so you search the front desk for the code.
#
# "In order to improve security," the document you find says, 
# "bathroom codes will no longer be written down. 
# Instead, please memorize and follow the procedure below to 
# access the bathrooms."
#
# The document goes on to explain that each button to be pressed can be 
# found by starting on the previous button and moving to adjacent buttons 
# on the keypad: U moves up, D moves down, L moves left, and R moves right. 
# Each line of instructions corresponds to one button, starting at the previous
# button (or, for the first line, the "5" button); press whatever button you're
# on at the end of each line. If a move doesn't lead to a button, ignore it.
#
# You can't hold it much longer, so you decide to figure out the code as 
# you walk to the bathroom. You picture a keypad like this:
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# Suppose your instructions are:
#
# ULL
# RRDDD
# LURDL
# UUUUD
#
# You start at "5" and move up (to "2"), left (to "1"), 
# and left (you can't, and stay on "1"), so the first button is 1.
# Starting from the previous button ("1"), you move right twice (to "3") 
# and then down three times (stopping at "9" after two moves and 
# ignoring the third), ending up with 9.
# Continuing from "9", you move left, up, right, down, and left, ending with 8.
# Finally, you move up four times (stopping at "2"), then down once, 
# ending with 5.
# So, in this example, the bathroom code is 1985.
# Your puzzle input is the instructions from the document you found at the 
# front desk. What is the bathroom code?
#
# --- Part Two ---
#
# You finally arrive at the bathroom (it's a several minute walk from the lobby
# so visitors can behold the many fancy conference rooms and water coolers on 
# this floor) and go to punch in the code. Much to your bladder's dismay, 
# the keypad is not at all like you imagined it. Instead, you are confronted 
# with the result of hundreds of man-hours of bathroom-keypad-design meetings:
#
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
#
# You still start at "5" and stop when you're at an edge, 
# but given the same instructions as above, the outcome is very different:
#
# You start at "5" and don't move at all (up and left are both edges), 
# ending at 5.
# Continuing from "5", you move right twice and down three times 
# (through "6", "7", "B", "D", "D"), ending at D.
# Then, from "D", you move five more times 
# (through "D", "B", "C", "C", "B"), ending at B.
#
# Finally, after five more moves, you end at 3.
# So, given the actual keypad layout, the code would be 5DB3.
#
# Using the same instructions in your puzzle input, 
# what is the correct bathroom code?
# ----------------------------------------------------------------------------

import re
import numpy as np

class BathroomCypher:

    def __init__(self, instructions, keypad):
        self.instructions = re.split('\n', instructions)
        self.keypad = keypad
        self.solution = []

    def solve_cypher(self):
        solution = [self.solve_line(x) for x in self.instructions]
        self.solution = [s for s in solution if s is not None]
        return self.solution

    def solve_line(self, instruction):
        if(instruction == ''):
            return None
        directions = list(instruction)
        for direction in directions:
            self.keypad.move(direction)
        return self.keypad.number()

class Keypad:

    def __init__(self):
        self.loc = (0, 0)

    def number(self):
        loc = self.loc
        if(loc == (-1, 1)):
            return 1
        elif(loc == (0, 1)):
            return 2
        elif(loc == (1, 1)):
            return 3
        elif(loc == (-1, 0)):
            return 4
        elif(loc == (0, 0)):
            return 5
        elif(loc == (1, 0)):
            return 6
        elif(loc == (-1, -1)):
            return 7
        elif(loc == (0, -1)):
            return 8
        elif(loc == (1, -1)):
            return 9

    def move(self, direction):
        tuple_dir = self.convert_direction(direction)
        self.loc = self.add_coordinates(self.loc, tuple_dir)
        return self.loc

    def convert_direction(self, direction):
        if(direction == 'U'):
            return (0, 1)
        elif(direction == 'D'):
            return (0, -1)
        elif(direction == 'L'):
            return (-1, 0)
        elif(direction == 'R'):
            return (1, 0)

    def add_coordinates(self, a, b):
        z = tuple(map(sum, zip(a, b)))
        return self.normalize(z)

    def normalize(self, coordinates):
        return tuple([x if abs(x) <= 1 else np.sign(x) for x in coordinates])

class Keypad2:
#       1
#     2 3 4
#   5 6 7 8 9
#     A B C
#       D
    move_hash = {
            (1, 'D'): 3,
            (2, 'D'): 6, (2, 'R'): 3,
            (3, 'U'): 1, (3, 'D'): 7, (3, 'L'): 2, (3, 'R'): 4,
            (4, 'D'): 8, (4, 'L'): 3,
            (5, 'R'): 6,
            (6, 'U'): 2, (6, 'D'): 'A', (6, 'L'): 5, (6, 'R'): 7,
            (7, 'U'): 3, (7, 'D'): 'B', (7, 'L'): 6, (7, 'R'): 8,
            (8, 'U'): 4, (8, 'D'): 'C', (8, 'L'): 7, (8, 'R'): 9,
            (9, 'L'): 8,
            ('A', 'U'): 6, ('A', 'R'): 'B',
            ('B', 'U'): 7, ('B', 'D'): 'D', ('B', 'L'): 'A', ('B', 'R'): 'C',
            ('C', 'U'): 8, ('C', 'L'): 'B',
            ('D', 'U'): 'B',
            }

    def __init__(self):
        self.loc = 5

    def move(self, direction):
        key = (self.loc, direction)
        if(key in Keypad2.move_hash):
            new_loc = Keypad2.move_hash[key]
        else:
            new_loc = self.loc
        self.loc = new_loc
        return self.loc

    def number(self):
        return self.loc

if __name__ == '__main__':
    fileobject = open('inputs/day02.txt')
    data = fileobject.read()
    bc = BathroomCypher(data, Keypad())
    bc.solve_cypher()
    print(bc.solution)
    # Correct answer is 69642
    bc2 = BathroomCypher(data, Keypad2())
    bc2.solve_cypher()
    print(bc2.solution)
    # Correct answer is 8CB23

