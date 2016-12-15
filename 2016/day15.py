# --- Day 15: Timing is Everything ---
#
# The halls open into an interior plaza containing a large kinetic sculpture. 
# The sculpture is in a sealed enclosure and seems to involve a set of 
# identical spherical capsules that are carried to the top and allowed to 
# bounce through the maze of spinning pieces.
#
# Part of the sculpture is even interactive! When a button is pressed, a 
# capsule is dropped and tries to fall through slots in a set of rotating discs
# to finally go through a little hole at the bottom and come out of the 
# sculpture. If any of the slots aren't aligned with the capsule as it passes, 
# the capsule bounces off the disc and soars away. You feel compelled to get 
# one of those capsules.
#
# The discs pause their motion each second and come in different sizes; they 
# seem to each have a fixed number of positions at which they stop. You decide 
# to call the position with the slot 0, and count up for each position it 
# reaches next.
#
# Furthermore, the discs are spaced out so that after you push the button, one 
# second elapses before the first disc is reached, and one second elapses as 
# the capsule passes from one disk to the one below it. So, if you push the 
# button at time=100, then the capsule reaches the top disc at time=101, the 
# second disc at time=102, the third disc at time=103, and so on.
#
# The button will only drop a capsule at an integer time - no fractional 
# seconds allowed.
#
# For example, at time=0, suppose you see the following arrangement:
#
# Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1.
#
# If you press the button exactly at time=0, the capsule would start to fall; 
# it would reach the first disc at time=1. Since the first disc was at 
# position 4 at time=0, by time=1 it has ticked one position forward. 
# As a five-position disc, the next position is 0, and the capsule falls 
# through the slot.
#
# Then, at time=2, the capsule reaches the second disc. The second disc has 
# ticked forward two positions at this point: it started at position 1, then 
# continued to position 0, and finally ended up at position 1 again. Because 
# there's only a slot at position 0, the capsule bounces away.
#
# If, however, you wait until time=5 to push the button, then when the capsule 
# reaches each disc, the first disc will have ticked forward 5+1 = 6 times 
# (to position 0), and the second disc will have ticked forward 5+2 = 7 times 
# (also to position 0). In this case, the capsule would fall through the discs 
# and come out of the machine.
#
# However, your situation has more than two discs; you've noted their positions
# in your puzzle input. What is the first time you can press the button to get 
# a capsule?
#
# Your puzzle answer was 203660.
#
# --- Part Two ---
#
# After getting the first capsule (it contained a star! what great fortune!), 
# the machine detects your success and begins to rearrange itself.
#
# When it's done, the discs are back in their original configuration as if it 
# were time=0 again, but a new disc with 11 positions and starting at 
# position 0 has appeared exactly one second below the previously-bottom disc.
#
# With this new disc, and counting again starting from time=0 with the 
# configuration in your puzzle input, what is the first time you can press the 
# button to get another capsule?
#
# -----------------------------------------------------------------------------

import re

def parse_line(line):
    positions = int(re.search('[0-9]+(?= positions)', line).group(0))
    start = int(re.search('(?<=position )[0-9]+', line).group(0))
    return positions, start

class Disc:
    
    def __init__(self, positions, start):
        self.positions = positions
        self.position = start
        self.start = start

    def __repr__(self):
        return str(self.position)

    def advance(self, n=1):
        self.position = ((n + self.position) % self.positions) 
        return self.position

class Sculpture:

    def __init__(self):
        self.discs = []
        self.time = 0

    def add_disc(self, disc):
        self.discs.append(disc)

    def reset_discs(self):
        for disc in self.discs:
            disc.position = disc.start

    def discs_at_drop_time(self, t):
        i = t
        pos = []
        for disc in self.discs:
           i += 1 
           pos.append(disc.advance(i))
        self.reset_discs()
        return pos

    def slots_line_up_at_drop_time(self, t):
        return sum(self.discs_at_drop_time(t)) == 0

    def solve(self):
        t = 0
        while not self.slots_line_up_at_drop_time(t):
            t += 1
        return t

if __name__ == '__main__':

    lines = open('inputs/day15.txt').read().splitlines()
    s = Sculpture()
    for line in lines:
        positions, start = parse_line(line)
        s.add_disc(Disc(positions, start))
    print('Part 1:', s.solve())
    s.add_disc(Disc(11, 0))
    print('Part 2:', s.solve())
