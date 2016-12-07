# --- Day 16: Aunt Sue ---
#
# Your Aunt Sue has given you a wonderful gift, and you'd like to send her a 
# thank you card. 
# However, there's a small problem: she signed it "From, Aunt Sue".
#
# You have 500 Aunts named "Sue".
#
# So, to avoid sending the card to the wrong person, you need to figure out 
# which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you 
# the gift. You open the present and, as luck would have it, good ol' Aunt Sue 
# got you a My First Crime Scene Analysis Machine! Just what you wanted. 
# Or needed, as the case may be.
#
# The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few
# specific compounds in a given sample, as well as how many distinct kinds of 
# those compounds there are. According to the instructions, these are what the 
# MFCSAM can detect:
#
# children, by human DNA age analysis.
# cats. It doesn't differentiate individual breeds.
# Several seemingly random dogs: samoyeds, pomeranians, akitas, and vizslas.
# goldfish. No other kinds of fish.
# trees, all in one group.
# cars, presumably by exhaust or gasoline or something.
# perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
# In fact, many of your Aunts Sue have many of these. You put the wrapping from
# the gift into the MFCSAM. It beeps inquisitively at you a few times and then 
# prints out a message on ticker tape:
#
# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1
#
# You make a list of the things you can remember about each Aunt Sue. Things 
# missing from your list aren't zero - you simply don't remember the value.
#
# What is the number of the Sue that got you the gift?
#
# -----------------------------------------------------------------------------

import re

MFCSAM_RESULTS = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes':1
        }

class Sue:
    
    def __init__(self, line):
        self.id, self.things = self.parse_things(line)

    def parse_things(self, things):
        d = {}
        items = re.findall('[a-zA-Z]+', things)
        values = re.findall('[0-9]+', things)
        for item, value in zip(items, values):
            d[item] = int(value)
        sue_id = d['Sue']
        del d['Sue']
        return sue_id, d

    def compare_things(self, other_things):
        result = []
        for key, value in self.things.items():
            if key in other_things:
               result.append(other_things[key] == value)
        return result

if __name__ == '__main__':
    fileobject = open('day16.txt')
    data = fileobject.read()
    lines = re.split('\n', data)
    sues = [Sue(line) for line in lines]
    for sue in sues:
        if len(sue.things) > 0:
            if all(sue.compare_things(MFCSAM_RESULTS)):
                print(sue.id)
