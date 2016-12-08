# --- Day 8: Two-Factor Authentication ---
#
# You come across a door implementing what you can only assume is an 
# implementation of two-factor authentication after a long game of requirements
# telephone.
#
# To get past the door, you first swipe a keycard (no problem; there was one on
# a nearby desk). Then, it displays a code on a little screen, and you type 
# that code on a keypad. Then, presumably, the door unlocks.
#
# Unfortunately, the screen has been smashed. After a few minutes, you've taken
# everything apart and figured out how it works. Now you just have to work out 
# what the screen would have displayed.
#
# The magnetic strip on the card you swiped encodes a series of instructions 
# for the screen; these instructions are your puzzle input. The screen is 50 
# pixels wide and 6 pixels tall, all of which start off, and is capable of 
# three somewhat peculiar operations:
#
# - rect AxB turns on all of the pixels in a rectangle at the top-left of the 
#    screen which is A wide and B tall.
# - rotate row y=A by B shifts all of the pixels in row A (0 is the top row) 
#   right by B pixels. Pixels that would fall off the right end appear at the 
#   left end of the row.
# - rotate column x=A by B shifts all of the pixels in column A (0 is the left 
#   column) down by B pixels. Pixels that would fall off the bottom appear at 
#   the top of the column.
#
# For example, here is a simple sequence on a smaller screen:
#
# rect 3x2 creates a small rectangle in the top-left corner:
#
# ###....
# ###....
# .......
#
# rotate column x=1 by 1 rotates the second column down by one pixel:
#
# #.#....
# ###....
# .#.....
#
# rotate row y=0 by 4 rotates the top row right by four pixels:
#
# ....#.#
# ###....
# .#.....
#
# rotate column x=1 by 1 again rotates the second column down by one pixel, 
# causing the bottom pixel to wrap back to the top:
#
# .#..#.#
# #.#....
# .#.....
#
# As you can see, this display technology is extremely powerful, and will soon 
# dominate the tiny-code-displaying-screen market. That's what the 
# advertisement on the back of the display tries to convince you, anyway.
#
# There seems to be an intermediate check of the voltage used by the display: 
# after you swipe your card, if the screen did work, how many pixels should be 
# lit?
#
# -----------------------------------------------------------------------------

import re

class Screen:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.screen = [[0 for x in range(w)] for y in range(h)]

    def __repr__(self):
        for row in self.screen:
            arr = ['' for i in range(len(row))]
            for i in range(len(row)):
                if (i+1) % 5 == 0 and i != 0:
                    arr[i] = ' | '
                elif row[i] == 1:
                    arr[i] = '0'
                else:
                    arr[i] = ' '
            print(''.join(arr))
        return ''

    def rect(self, A, B):
        for j in range(B):
            for i in range(A):
                self.screen[j][i] = 1

    def rotate_row(self, y, num):
        row = self.screen[y]
        new_row = [0 for x in range(len(row))]
        for i in range(len(row)):
            new_row[(i+num) % len(row)] = row[i]
        self.screen[y] = new_row

    def rotate_column(self, x, num):
        screen = self.screen
        n_rows = len(screen)
        col = [screen[j][x] for j in range(n_rows)]
        new_col = [0 for y in range(n_rows)]
        for j in range(n_rows):
            screen[(j+num) % n_rows][x] = col[j]
        self.screen = screen

    def sum(self):
        screen = self.screen
        w = self.width
        h = self.height
        return sum([sum([screen[j][i] for i in range(w)]) for j in range(h)])

class Instruction:

    def __init__(self, raw_text):
        self.raw = raw_text

    def parse(self):
        text = self.raw
        function = re.search('rect|row|column', text).group(0)
        if(function == 'rect'):
            A = int(re.search('[0-9]+(?=x)', text).group(0))
            B = int(re.search('(?<=x)[0-9]+', text).group(0))
            return function, A, B
        else:
            xy = int(re.search('(?<=\=)[0-9]+', text).group(0))
            n = int(re.search('[0-9]+$', text).group(0))
            return function, xy, n

if __name__ == '__main__':
    fileobject = open('inputs/day08.txt')
    data = fileobject.read()
    lines = re.split('\n', data)
    s = Screen(50, 6)
    instructions = [Instruction(l).parse() for l in lines]
    for inst in instructions:
        if(inst[0] == 'rect'):
            s.rect(inst[1], inst[2])
        elif(inst[0] == 'row'):
            s.rotate_row(inst[1], inst[2])
        elif(inst[0] == 'column'):
            s.rotate_column(inst[1], inst[2])
    print("Part 1:", s.sum())
    # Correct answer is 121
    print("Part 2:")
    print(s)
    # Correct answer is RURUCEOEIL
