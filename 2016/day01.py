# --- Day 1: No Time for a Taxicab ---
#
# Santa's sleigh uses a very high-precision clock to guide its movements, 
# and the clock's oscillator is regulated by stars. 
# Unfortunately, the stars have been stolen... by the Easter Bunny. 
# To save Christmas, Santa needs you to retrieve all fifty stars by 
# December 25th.
#
# Collect stars by solving puzzles. 
# Two puzzles will be made available on each day in the advent calendar; 
# the second puzzle is unlocked when you complete the first. 
# Each puzzle grants one star. Good luck!
#
# You're airdropped near Easter Bunny Headquarters in a city somewhere. 
# "Near", unfortunately, is as close as you can get - the instructions 
# on the Easter Bunny Recruiting Document the Elves intercepted start here, 
# and nobody had time to work them out further.
#
# The Document indicates that you should start at the given coordinates 
# (where you just landed) and face North. Then, follow the provided sequence: 
# either turn left (L) or right (R) 90 degrees, 
# then walk forward the given number of blocks, ending at a new intersection.
#
# There's no time to follow such ridiculous instructions on foot, 
# though, so you take a moment and work out the destination. 
# Given that you can only walk on the street grid of the city, 
# how far is the shortest path to the destination?
# 
# For example:
#
# Following R2, L3 leaves you 2 blocks East and 3 blocks North, 
# or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, 
# which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?
#
# Your puzzle answer was 246.
#
# --- Part Two ---
#
# Then, you notice the instructions continue on the back of the 
# Recruiting Document. 
# Easter Bunny HQ is actually at the first location you visit twice.
#
# For example, if your instructions are R8, R4, R4, R8, 
# the first location you visit twice is 4 blocks away, due East.
#
# How many blocks away is the first location you visit twice?
#
# Your puzzle answer was 124.
# ----------------------------------------------------------------------------

import re

f = open('inputs/day01.txt', 'r')
data = f.read()

class Location:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cardinal = 'North'
        self.next_move = None
        self.previous_locations = []
    
    def current_location(self):
        return (self.x, self.y)

    def parse_move(self, string):
        direction = re.search('R|L', string).group(0)
        distance = int(re.search('[0-9]+', string).group(0))
        self.next_move = (direction, distance)
        return self.next_move

    def move(self, direction=None, distance=None):
        if(direction is None):
            direction = self.next_move[0]
        if(distance is None):
            distance = self.next_move[1]
        self.turn(direction)
        for i in range(distance):
            self.move1(self.cardinal)
        self.next_move = None
        return (self.current_location())

    def move1(self, cardinal):
        self.previous_locations.append(self.current_location())
        if(cardinal == 'North'):
            self.y = self.y + 1
        elif(cardinal == 'South'):
            self.y = self.y - 1
        elif(cardinal == 'East'):
            self.x = self.x + 1
        elif(cardinal == 'West'):
            self.x = self.x - 1
        
    def turn(self, direction):
        cardinal = self.cardinal
        if(cardinal == 'North'):
            if(direction == 'R'):
               cardinal = 'East'
            elif(direction == 'L'):
                cardinal = 'West'
        elif(cardinal == 'South'):
            if(direction == 'R'): 
                cardinal = 'West'
            elif(direction == 'L'):
                cardinal = 'East'
        elif(cardinal == 'East'):
            if(direction == 'R'):
                cardinal = 'South'
            elif(direction == 'L'):
                cardinal = 'North'
        elif(cardinal == 'West'):
            if(direction == 'R'):
                cardinal = 'North'
            elif(direction == 'L'):
                cardinal = 'South'
        self.cardinal = cardinal
        return self.cardinal

if __name__ == '__main__':
    f = open('inputs/day01.txt')
    data = f.read()
    moves = re.split(',', data)
    bunny = Location()

    # Part 1, go through all the moves
    for move in moves:
        bunny.parse_move(move)
        bunny.move()
    print(abs(bunny.x) + abs(bunny.y))
    # Correct answer is 246

    # Part 2, find first overlapping location
    for i in reversed(range(len(bunny.previous_locations))):
        if(bunny.previous_locations[i] in bunny.previous_locations[0:(i-1)]):
            print(True)
        print(bunny.previous_locations[i])
    # Corrdinates are printed to the screen. I had to scroll through the 
    # printout to find the right one. 
    # Correct answer is (-109, -15), or 124
