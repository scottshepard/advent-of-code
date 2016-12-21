# --- Day 19: An Elephant Named Joseph ---
#
# The Elves contact you over a highly secure emergency channel. Back at the 
# North Pole, the Elves are busy misunderstanding White Elephant parties.
#
# Each Elf brings a present. They all sit in a circle, numbered starting with 
# position 1. Then, starting with the first Elf, they take turns stealing all 
# the presents from the Elf to their left. An Elf with no presents is removed 
# from the circle and does not take turns.
#
# For example, with five Elves (numbered 1 to 5):
#
#   1
# 5   2
#  4 3
#
# Elf 1 takes Elf 2's present.
# Elf 2 has no presents and is skipped.
# Elf 3 takes Elf 4's present.
# Elf 4 has no presents and is also skipped.
# Elf 5 takes Elf 1's two presents.
# Neither Elf 1 nor Elf 2 have any presents, so both are skipped.
# Elf 3 takes Elf 5's three presents.
# So, with five Elves, the Elf that sits starting in position 3 gets all the 
# presents.
#
# With the number of Elves given in your puzzle input, which Elf gets all the 
# presents?
#
# ----------------------------------------------------------------------------
# 
# My original attempt at this was to actually similate all the elves stealing 
# from each other and track the number of presents each elf had. That approach
# worked fine for small circles but it was going to take ~4.5 hours with 
# my input string. 
#
# It took me a while to figure out the pattern, but each "round" depending on 
# if the first elf gets to steal or is stolen from, you can simply remove
# all the even or odd indicies elves. If the first elf gets to go, remove
# all the odd indicies. If the first elf does not get to go, remove all
# the even indicies.
#
# You can tell what's going to happen on next round depending on the state of 
# the current round. If the number of elves in the cirle is odd, the starting 
# elf will flip (if the first elf did get to go then he gets stolen from 
# next round), while if the number of elves in the cirle is even, whatever
# happens this round stays. This is a bit esoterically coded up in the
# next_start function.

class Day19:

    def __init__(self, n_elves):
        self.n_elves = n_elves
        self.elves = list(range(1, n_elves+1))
        self.start = 0

    def next_start(self):
        start = self.start
        if self.len_elves_is_even():
            if start == 0:
                return 0
            else:
                return 1
        else:
            if start == 0:
                return 1
            else:
                return 0

    def len_elves_is_even(self):
        return len(self.elves) % 2 == 0

    def steal_presents(self):
        next_start = self.next_start()
        # self.start is either 0 or 1, indicating that either even or odd
        # indexed elves should be kept
        self.elves = [x for i, x in enumerate(self.elves) if i % 2 == self.start]
        self.start = next_start
        return self.elves

    def solve(self):
        while len(self.elves) > 1:
            self.steal_presents()
        return self.elves[0]

    def index_across(self, i):
        len_ = len(self.elves)
        i = i % len_
        return int(len_ / 2 + i) % len_

    def steal_presents2(self, i):
        self.elves.pop(self.index_across(i))

    def solve2(self):
        i = 0
        while len(self.elves) > 1:
            self.steal_presents2(i)
            len_ = len(self.elves)
            if i == len_:
                i = 0
            else:
                i += 1
            if len_ % 10000 == 0:
                print('There are', len(self.elves), 'elves left', end='\r')
        return self.elves[0]

if __name__ == '__main__':
    input1 = 3014603
    assert(Day19(5).solve() == 3)
    assert(Day19(7).solve() == 7)
    print('Part 1:', Day19(input1).solve())
    assert(Day19(5).solve2() == 2)
    assert(Day19(7).solve2() == 5)
