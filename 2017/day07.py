# --- Day 7: Recursive Circus ---
# Wandering further through the circuits of the computer, you come upon a tower
# of programs that have gotten themselves into a bit of trouble. A recursive
# algorithm has gotten out of hand, and now they're balanced precariously
# in a large tower.
#
# One program at the bottom supports the entire tower.
# It's holding a large disc, and on the disc are balanced several more 
# sub-towers. At the bottom of these sub-towers, standing on the bottom disc,
# are other programs, each holding their own disc, and so on. At the very tops
# of these sub-sub-sub-...-towers, many programs stand simply keeping the disc
# below them balanced but with no disc of their own.
#
# You offer to help, but first you need to understand the structure of these
# towers. You ask each program to yell out their name, their weight,
# and (if they're holding a disc) the names of the programs immediately above
# them balancing on that disc. You write this information down
# (your puzzle input). Unfortunately, in their panic, they don't do this in an
# orderly fashion; by the time you're done, you're not sure which program gave
# which information.
#
# For example, if your list is the following:
#
# pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)
#
# ...then you would be able to recreate the structure of the towers that 
# looks like this:
#
#                 gyxo
#               /     
#          ugml - ebii
#        /      \     
#       |         jptl
#       |        
#       |         pbga
#      /        /
# tknk --- padx - havc
#      \        \
#       |         qoyq
#       |             
#       |         ktlj
#        \      /     
#          fwft - cntj
#               \     
#                 xhth
#
# In this example, tknk is at the bottom of the tower (the bottom program),
# and is holding up ugml, padx, and fwft. Those programs are, in turn, holding
# up other programs; in this example, none of those programs are holding up any
# other programs, and are all the tops of their own towers. (The actual tower
# balancing in front of you is much larger.)
#
# Before you're ready to help them, you need to make sure your information is 
# correct. What is the name of the bottom program?
#
# To begin, get your puzzle input.
# Answer: wiapj
#
# 
# --- Part Two ---
#
# The programs explain the situation: they can't get down. Rather, they could
# get down, if they weren't expending all of their energy trying to keep the
# tower balanced. Apparently, one program has the wrong weight, and until it's
# fixed, they're stuck here.
#
# For any program holding a disc, each program standing on that disc forms a
# sub-tower. Each of those sub-towers are supposed to be the same weight, 
# or the disc itself isn't balanced. The weight of a tower is the sum of the
# weights of the programs in that tower.
#
# In the example above, this means that for ugml's disc to be balanced, gyxo,
# ebii, and jptl must all have the same weight, and they do: 61.
#
# However, for tknk to be balanced, each of the programs standing on its disc
# and all programs above it must each match. This means that the following sums
# must all be the same:
#
# ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
# padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
# fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
# 
# As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
# other two. Even though the nodes above ugml are balanced,
# ugml itself is too heavy: it needs to be 8 units lighter for its stack to
# weigh 243 and keep the towers balanced. If this change were made, its weight
# would be 60.
#
# Given that exactly one program is the wrong weight, what would its weight 
# need to be to balance the entire tower?
# Answer: 1072
#
# ------------------------------------------------------------------------------

import os
import re

class Tower:

    def __init__(self, lines):
        self.lines = lines
        self.programs = {}

    def solve1(self):
        self.parse_lines()
        return self.find_root()

    def parse_lines(self):
        for line in self.lines:
            self.parse_line(line)
        return self.programs

    def parse_line(self, line):
        names = re.findall('[a-z]+', line)
        weight = re.search('[0-9]+', line).group(0)
        root_name = names[0]
        names.pop(0)
        if root_name not in self.programs.keys():
            self.programs[root_name] = Program(root_name)
        if len(names) > 0:
            for child_name in names:
                if(child_name not in self.programs.keys()):
                    self.programs[child_name] = Program(child_name)
                self.programs[child_name].add_parent(self.programs[root_name])
                self.programs[root_name].add_child(self.programs[child_name])
        self.programs[root_name].set_weight(weight)

    def find_root(self, prog = ''):
        if prog == '':
            prog = next(iter(tower.programs.values()))
        if prog.is_root():
            self.root = prog
            return self.root
        else:
            return self.find_root(prog.parent)

    def total_weight(self):
        return self.root.total_weight()

    def is_balanced(self):
        return self.root.is_balanced()

    def balance(self):
        return self.root.balance()

class Program:

    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = 0
        self.weight = 0

    def __repr__(self):
        return self.name

    def add_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def set_weight(self, weight):
        self.weight = int(weight)

    def is_root(self):
        return self.parent == 0

    def total_weight(self):
        self.total_weight = self.weight + sum([c.total_weight() for c in self.children])
        return self.total_weight

    def is_balanced(self):
        lst = [c.total_weight for c in self.children]
        return lst[1:] == lst[:-1]

    def balance(self, n=0):
        if self.is_balanced():
            return self.weight - n
        else:
            weights = [c.total_weight for c in self.children]
            maxw = max(weights)
            minw = min(weights)
            heaviest = [c for c in self.children if c.total_weight == maxw][0]
            return heaviest.balance(maxw-minw)

if __name__ == '__main__':    
    rel_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(rel_path, "inputs/day07.txt")
    f = open(file_path)
    data = f.read().split('\n')
    tower = Tower(data)
    print(tower.solve1())
    tower.total_weight()
    print(tower.balance())
