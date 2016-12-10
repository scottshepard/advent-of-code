# --- Day 10: Balance Bots ---
#
# You come upon a factory in which many robots are zooming around handing small
# microchips to each other.
#
# Upon closer examination, you notice that each bot only proceeds when it has 
# two microchips, and once it does, it gives each one to a different bot or 
# puts it in a marked "output" bin. Sometimes, bots take microchips from 
# "input" bins, too.
#
# Inspecting one of the microchips, it seems like they each contain a single 
# number; the bots must use some logic to decide what to do with each chip. 
# You access the local control computer and download the bots' instructions 
# (your puzzle input).
#
# Some of the instructions specify that a specific-valued microchip should be 
# given to a specific bot; the rest of the instructions indicate what a given 
# bot should do with its lower-value or higher-value chip.
#
# For example, consider the following instructions:
#
# value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
# value 3 goes to bot 1
# bot 1 gives low to output 1 and high to bot 0
# bot 0 gives low to output 2 and high to output 0
# value 2 goes to bot 2
#
# Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2
# chip and a value-5 chip.
# Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its
# higher one (5) to bot 0.
# Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and 
# gives the value-3 chip to bot 0.
# Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in 
# output 0.
# In the end, output bin 0 contains a value-5 microchip, output bin 1 contains 
# a value-2 microchip, and output bin 2 contains a value-3 microchip. In this 
# configuration, bot number 2 is responsible for comparing value-5 microchips 
# with value-2 microchips.
#
# Based on your instructions, what is the number of the bot that is responsible
# for comparing value-61 microchips with value-17 microchips?
# 
# -----------------------------------------------------------------------------

import re

class Bot:

    def __init__(self, id_, type_='bot'):
        self.id_ = id_
        self.chips = []
        self.name = type_ + ' ' + str(id_)

    def __repr__(self):
        return self.name

    def move(self):
        if self.at_capacity():
            if self.chips == [17, 61]:
                print('Part 1:', self.name, 'compares chip', 
                      self.chips[0], 'to chip', self.chips[1])
            self.give_low()
            self.give_high()

    def add_chip(self, chip):
        self.chips.append(chip)
        self.chips.sort()

    def set_low(self, bot):
        self.low_to = bot 

    def set_high(self, bot):
        self.high_to = bot

    def at_capacity(self):
        return len(self.chips) == 2

    def give_low(self):
        return self.low_to.add_chip(self.chips.pop(0))

    def give_high(self):
        return self.high_to.add_chip(self.chips.pop(-1))

class Day10:

    def __init__(self, data):
        self.lines = re.split('\n', data)
        self.bots = []
        self.bins = []

    def add_bots(self):
        for line in self.lines:
            bot_id = int(re.search('(?<=bot )[0-9]+', line).group(0))
            bin_ids = re.findall('(?<=output )[0-9]+', line)
            if bot_id not in [bot.id_ for bot in self.bots]:
                self.bots.append(Bot(bot_id))
            for bin_id in bin_ids:
                bin_id = int(bin_id)
                if bin_id not in [bin_.id_ for bin_ in self.bins]:
                    self.bins.append(Bot(bin_id, 'bin'))
            bot = self.find_bot(bot_id)
            value = re.search('(?<=value )[0-9]+', line)
            if value is not None:
                bot.add_chip(int(value.group(0)))
    
    def establish_rules(self):
        for line in self.lines:
            if re.search('value', line) is None:
                bot_id = int(re.search('(?<=bot )[0-9]+', line).group(0))
                bot = self.find_bot(bot_id)
                low  = re.search('(?<=low to )[a-z]+ [0-9]+', line).group(0)
                high = re.search('(?<=high to )[a-z]+ [0-9]+', line).group(0)
                low_id = int(re.search('[0-9]+', low).group(0))
                high_id = int(re.search('[0-9]+', high).group(0))
                low_to = re.search('output|bot', low).group(0)
                high_to = re.search('output|bot', high).group(0)
                if low_to == 'bot':
                    bot.set_low(self.find_bot(low_id))
                elif low_to == 'output':
                    bot.set_low(self.find_bin(low_id))
                if high_to == 'bot':
                    bot.set_high(self.find_bot(high_id))
                elif high_to == 'output':
                    bot.set_high(self.find_bin(high_id))

    def proceed(self):
        while any([bot.at_capacity() for bot in self.bots]):
            [bot.move() for bot in self.bots if bot.at_capacity()]

    def find_bot(self, bot_id):
        return [bot for bot in self.bots if bot.id_ == bot_id][0]

    def find_bin(self, bin_id):
        return [bin_ for bin_ in self.bins if bin_.id_ == bin_id][0]

    def part2(self, bin_ids):
        product = 1
        for bin_id in bin_ids:
            product = day10.find_bin(bin_id).chips[0] * product
        return product

if __name__ == '__main__':
    data = open('inputs/day10.txt').read()
    day10 = Day10(data)
    day10.add_bots()
    day10.establish_rules()
    day10.proceed()
    # Part 1 will print out on the screen. 
    # Correct answer is bot 101
    bins = day10.bins
    

