# --- Day 13: Knights of the Dinner Table ---
#
# In years past, the holiday feast with your family hasn't gone so well. 
# Not everyone gets along! This year, you resolve, will be different. 
# You're going to find the optimal seating arrangement and avoid all those 
# awkward conversations.
#
# You start by writing up a list of everyone invited and the amount their 
# happiness would increase or decrease if they were to find themselves sitting 
# next to each other person. You have a circular table that will be just big 
# enough to fit everyone comfortably, and so each person will have exactly two 
# neighbors.
#
# For example, suppose you have only four attendees planned, and you calculate 
# their potential happiness as follows:
#
# Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol.
#
# Then, if you seat Alice next to David, Alice would lose 2 happiness units 
# (because David talks so much), but David would gain 46 happiness units 
# (because Alice is such a good listener), for a total change of 44.
#
# If you continue around the table, you could then seat Bob next to Alice 
# (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob 
# (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). 
# The arrangement looks like this:
#
#      +41 +46
# +55   David    -2
# Carol       Alice
# +60    Bob    +54
#      -7  +83
#
# After trying every other seating arrangement in this hypothetical scenario, 
# you find that this one is the most optimal, with a total change in happiness 
# of 330.
#
# What is the total change in happiness for the optimal seating arrangement of 
# the actual guest list?
#
# --- Part Two ---
#
# In all the commotion, you realize that you forgot to seat yourself. 
# At this point, you're pretty apathetic toward the whole thing, and your 
# happiness wouldn't really go up or down regardless of who you sit next to. 
# You assume everyone else would be just as ambivalent about sitting next to 
# you, too.
#
# So, add yourself to the list, and give all happiness relationships that 
# involve you a score of 0.
#
# What is the total change in happiness for the optimal seating arrangement 
# that actually includes yourself?
#
# -----------------------------------------------------------------------------

import re
from itertools import permutations 
from collections import deque

class Person:

    gain_loss_table = {'gain': +1, 'lose': -1}

    def __init__(self, name):
        self.name = name
        self.rules = {}

    def add_rule(self, rule):
        name = re.match('^[a-zA-Z]+', rule).group(0)
        if(name == self.name):
            direction = re.search('gain|lose', rule).group(0)
            sign = self.gain_loss_table[direction]
            happiness = int(re.search('[0-9]+', rule).group(0)) * sign
            sitnextto = re.search('[a-zA-Z]+(?=\.)', rule).group(0)
            self.rules[sitnextto] = happiness

    def happiness(self, name1, name2):
        rules = self.rules 
        return rules[name1] + rules[name2]

class Table:

    def __init__(self, size):
        self.spots = []

    def add_person(self, person):
        self.spots.append(person)

    def happiness(self):
        sum_happiness = 0
        size = len(self.spots)
        for i in range(size):
            p0 = self.spots[i-1]
            p1 = self.spots[i]
            p2 = self.spots[(i+1) % size]
            sum_happiness += p1.happiness(p0.name, p2.name)
        return sum_happiness

if __name__ == '__main__':
    fileobject = open('day13.txt')
    data = fileobject.read()
    rules = data.split('\n')
    names = set([re.match('[a-zA-Z]+', r).group(0) for r in rules])
    people = []
    for name in names:
        people.append(Person(name))
    for person in people:
        for rule in rules:
            person.add_rule(rule)
    perms = permutations(range(0, len(names))) 
    tables = []
    for perm in perms:
        table = Table(len(names))
        for i in perm:
            table.add_person(people[i])
        tables.append(table)
    print("Part 1:", max([x.happiness() for x in tables]))

    me = Person("Scott")
    for name in names:
        me.add_rule("Scott gain 0 " + name + ".")
    perms = permutations(range(0, len(names)+1)) 
    tables = []
    people.append(me)
    for perm in perms:
        table = Table(len(names)+1)
        for i in perm:
            table.add_person(people[i])
        tables.append(table)
    print("Part 2:", max([x.happiness() for x in tables]))


