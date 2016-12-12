# --- Day 11: Radioisotope Thermoelectric Generators ---
#
# You come upon a column of four floors that have been entirely sealed off from
# the rest of the building except for a small dedicated lobby. There are some 
# radiation warnings and a big sign which reads "Radioisotope Testing Facility"
#
# According to the project status board, this facility is currently being used 
# to experiment with Radioisotope Thermoelectric Generators (RTGs, or simply 
# "generators") that are designed to be paired with specially-constructed 
# microchips. Basically, an RTG is a highly radioactive rock that generates 
# electricity through heat.
#
# The experimental RTGs have poor radiation containment, so they're dangerously
# radioactive. The chips are prototypes and don't have normal radiation 
# shielding, but they do have the ability to generate an elecromagnetic 
# radiation shield when powered. Unfortunately, they can only be powered by 
# their corresponding RTG. An RTG powering a microchip is still dangerous to 
# other microchips.
#
# In other words, if a chip is ever left in the same area as another RTG, and 
# it's not connected to its own RTG, the chip will be fried. Therefore, it is 
# assumed that you will follow procedure and keep chips connected to their 
# corresponding RTG when they're in the same room, and away from other RTGs 
# otherwise.
#
# These microchips sound very interesting and useful to your current 
# activities, and you'd like to try to retrieve them. The fourth floor of the 
# facility has an assembling machine which can make a self-contained, shielded 
# computer for you to take with you - that is, if you can bring it all of the 
# RTGs and microchips.
#
# Within the radiation-shielded part of the facility (in which it's safe to 
# have these pre-assembly RTGs), there is an elevator that can move between the
# four floors. Its capacity rating means it can carry at most yourself and two 
# RTGs or microchips in any combination. (They're rigged to some heavy 
# diagnostic equipment - the assembling machine will detach it for you.) As a 
# security measure, the elevator will only function if it contains at least one
# RTG or microchip. The elevator always stops on each floor to recharge, and 
# this takes long enough that the items within it and the items on that floor 
# can irradiate each other. (You can prevent this if a Microchip and its 
# Generator end up on the same floor in this way, as they can be connected 
# while the elevator is recharging.)
#
#
# You make some notes of the locations of each component of interest 
# (your puzzle input). Before you don a hazmat suit and start moving things 
# around, you'd like to have an idea of what you need to do.
#
# When you enter the containment area, you and the elevator will start on the 
# first floor.
#
# For example, suppose the isolated area has the following arrangement:
#
# The first floor contains a hydrogen-compatible microchip and a 
# lithium-compatible microchip.
#
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.
# As a diagram (F# for a Floor number, E for Elevator, H for Hydrogen, L for 
# Lithium, M for Microchip, and G for Generator), the initial state looks like 
# this:
#
# F4 .  .  .  .  .  
# F3 .  .  .  LG .  
# F2 .  HG .  .  .  
# F1 E  .  HM .  LM 
#
# Then, to get everything up to the assembling machine on the fourth floor, the
# following steps could be taken:
#
# Bring the Hydrogen-compatible Microchip to the second floor, which is safe 
# because it can get power from the Hydrogen Generator:
#
# F4 .  .  .  .  .  
# F3 .  .  .  LG .  
# F2 E  HG HM .  .  
# F1 .  .  .  .  LM 
#
# Bring both Hydrogen-related items to the third floor, which is safe because 
# the Hydrogen-compatible microchip is getting power from its generator:
#
# F4 .  .  .  .  .  
# F3 E  HG HM LG .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  LM 
#
# Leave the Hydrogen Generator on floor three, but bring the 
# Hydrogen-compatible Microchip back down with you so you can still use the 
# elevator:
#
# F4 .  .  .  .  .  
# F3 .  HG .  LG .  
# F2 E  .  HM .  .  
# F1 .  .  .  .  LM 
#
# At the first floor, grab the Lithium-compatible Microchip, which is safe 
# because Microchips don't affect each other:
#
# F4 .  .  .  .  .  
# F3 .  HG .  LG .  
# F2 .  .  .  .  .  
# F1 E  .  HM .  LM 
#
# Brith both Microchips up one floor, where there is nothing to fry them:
#
# F4 .  .  .  .  .  
# F3 .  HG .  LG .  
# F2 E  .  HM .  LM 
# F1 .  .  .  .  .  
#
# Bring both Microchips up again to floor three, where they can be temporarily 
# connected to their corresponding generators while the elevator recharges, 
# preventing either of them from being fried:
#
# F4 .  .  .  .  .  
# F3 E  HG HM LG LM 
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
#
# Bring both Microchips to the fourth floor:
#
# F4 E  .  HM .  LM 
# F3 .  HG .  LG .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
#
# Leave the Lithium-compatible microchip on the fourth floor, but bring the 
# Hydrogen-compatible one so you can still use the elevator; this is safe 
# because although the Lithium Generator is on the destination floor, you can 
# connect Hydrogen-compatible microchip to the Hydrogen Generator there:
#
# F4 .  .  .  .  LM 
# F3 E  HG HM LG .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
#
# Bring both Generators up to the fourth floor, which is safe because you can 
# connect the Lithium-compatible Microchip to the Lithium Generator upon 
# arrival:
#
# F4 E  HG .  LG LM 
# F3 .  .  HM .  .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
#
# Bring the Lithium Microchip with you to the third floor so you can use the 
# elevator:
#
# F4 .  HG .  LG .  
# F3 E  .  HM .  LM 
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
#
# Bring both Microchips to the fourth floor:
#
# F4 E  HG HM LG LM 
# F3 .  .  .  .  .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
#
# In this arrangement, it takes 11 steps to collect all of the objects at the 
# fourth floor for assembly. (Each elevator stop counts as one step, even if 
# nothing is added to or removed from it.)
#
# In your situation, what is the minimum number of steps required to bring all 
# of the objects to the fourth floor?
#
#
# -----------------------------------------------------------------------------

from itertools import combinations
import re

class MicroGen:
    '''This object could be either a microchip or a generator'''

    def __init__(self, element, type_, position):
        self.element = element
        self.type_ = type_
        self.name = (element[0] + type_[0]).upper()
        self.position = position

    def __repr__(self):
        return self.name

    def compatible(self, other):
        if other.type_ == self.type_:
            return True
        else:
            return self.element == other.element

class Floor:

    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.things = ['.'] * size

    def __repr__(self):
        return ' '.join(['F' + str(self.number)] + 
                [str(t) for t in self.things])

    def add_thing(self, thing):
        self.things[thing.position] = thing

    def remove_thing(self, position):
        self.things[position] = '.'

    def remove_elevator(self):
        if self.has_elevator():
            self.remove_thing(0)
        else:
            raise LookupError('This floor does not have an elevator to remove')

    def has_elevator(self):
        return type(self.things[0]) is Elevator

    def load_elevator(self, thing):
        if self.has_elevator():
            elevator = self.things[0]
            elevator.add_thing(thing)
        else:
            raise LookupError('This floor does not have an elevator to load')

    def clear_floor(self):
        if self.has_elevator():
            elevator = self.things[0]
            for thing in elevator.things:
                self.remove_thing(thing.postion)
        else:
            raise LookupError('This floor does not have an elevator ' + 
                              'so the floor cannot be cleared.')

    def is_valid(self):
        things = [thing for thing in self.things if type(thing) is MicroGen]
        bools = []
        for combo in combinations(things, 2):
            bools.append(combo[0].compatible(combo[1]))
        return all(bools)

class Elevator:

    def __init__(self):
        self.position = 0
        self.things = []

    def __str__(self):
        return 'E'

    def add_thing(self, thing):
        if self.at_capacity():
            return False
        else:
            self.things.append(thing)
            return True

    def at_capacity(self):
        return len(self.things) == 2

class Building:

    def __init__(self, n_floors):
        self.floors = [None] * n_floors

    def __repr__(self):
        return '\n'.join([f.__repr__() for f in reversed(self.floors)])

    def add_floor(self, floor):
        self.floors[floor.number-1] = floor

    def add_elevator(self, start_floor=1):
        self.floor(start_floor).add_thing(Elevator())
        self.elevator_floor = self.floor(start_floor)

    def floor(self, number):
        return self.floors[number - 1]

    def move_elevator(self, direction):
        next_floor_num = self.elevator_floor.number + direction
        if next_floor_num >= 0 and next_floor_num <= len(self.floors):
            next_floor = self.floor(next_floor_num)
            elevator_floor = self.elevator_floor
            elevator = elevator_floor.things[0]
            elevator_floor.remove_elevator()
            next_floor.add_thing(elevator)
            self.elevator_floor = next_floor
        else:
            raise IndexError('Cannot move in that direction anymore')

    def is_valid(self):
        return all([floor.is_valid() for floor in self.floors])

if __name__ == '__main__':
    data = open('inputs/day11_test.txt').read()
    lines = data.splitlines()

    # Test input is hard coded. 
    # TODO: building a parser class for input instructions
    building = Building(4)
    building.add_floor(Floor(1, 5))
    building.add_floor(Floor(2, 5))
    building.add_floor(Floor(3, 5))
    building.add_floor(Floor(4, 5))
    building.add_elevator()
    building.floor(1).add_thing(MicroGen('hydrogen', 'microchip', 2))
    building.floor(1).add_thing(MicroGen('lithium', 'microchip', 4))
    building.floor(2).add_thing(MicroGen('hydrogen', 'generator', 1))
    building.floor(3).add_thing(MicroGen('lithium', 'generator', 3))


