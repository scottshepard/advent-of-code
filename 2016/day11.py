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
# -----------------------------------------------------------------------------

from copy import deepcopy
from itertools import combinations
import re

def flatten(x):
    return sum(x, [])

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

class Elevator:

    def __init__(self):
        self.position = 0
        self.things = []

    def __str__(self):
        return 'E'

    def __eq__(self, other):
        return type(self) is type(other)

    def add_thing(self, thing):
        if self.at_capacity():
            return False
        else:
            self.things.append(thing)
            return True

    def remove_all_things(self):
        while len(self.things) > 0:
            self.things.pop()

    def at_capacity(self):
        return len(self.things) == 2

    def is_valid(self):
        if len(self.things) in [0, 1]:
            return True
        else:
            return self.things[0].compatible(self.things[1])

class Floor:

    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.things = ['.'] * size
        self.microchips = []
        self.generators = []

    def __repr__(self):
        return ' '.join(['F' + str(self.number)] + 
                [str(t) for t in self.things])

    def __eq__(self, other):
        return all([self.things[i] == other.things[i] for i in range(0, 5)])

    def add_thing(self, thing):
        self.things[thing.position] = thing
        if type(thing) is MicroGen:
            if thing.type_ == 'microchip':
                self.microchips.append(thing)
            elif thing.type_ == 'generator':
                self.generators.append(thing)

    def remove_thing(self, position):
        thing = self.things[position]
        self.things[position] = '.'
        if type(thing) is MicroGen:
            if thing.type_ == 'microchip':
                self.microchips = [m for m in self.microchips if m != thing]
            elif thing.type_ == 'generator':
                self.generators = [g for g in self.generators if g != thing]

    def non_lift_things(self):
        return [thing for thing in self.things if type(thing) is MicroGen]

    def n_things(self):
        return len(self.non_lift_things())

    def remove_elevator(self):
        if self.has_elevator():
            self.remove_thing(0)
        else:
            raise LookupError('This floor does not have an elevator to remove')

    def has_elevator(self):
        return type(self.things[0]) is Elevator

    def elevator(self):
        if self.has_elevator():
            return self.things[0]
        else:
            raise LookupError('This floor does not have an elevator')

    def load_elevator(self, thing):
        if self.has_elevator():
            elevator = self.elevator()
            elevator.add_thing(thing)
            self.remove_thing(thing.position)
        else:
            raise LookupError('This floor does not have an elevator to load')

    def unload_elevator(self):
        if self.has_elevator():
            if self.elevator().things:
                for thing in self.elevator().things:
                    self.add_thing(thing)
                self.elevator().remove_all_things()

    def is_valid(self):
        bools = []
        microchips = [m.element for m in self.microchips]
        generators = [g.element for g in self.generators]
        for g in generators:
            for m in microchips:
                if m != g and m not in generators:
                    return False
        return True

    def is_full(self):
        return all([type(thing) is MicroGen for thing in self.things])

    def thing_combos(self):
        return combinations(self.non_lift_things(), 2)

class Building:

    def __init__(self, n_floors):
        self.floors = [None] * n_floors

    def __repr__(self):
        return '\n'.join([f.__repr__() for f in reversed(self.floors)])

    def __eq__(self, other):
        bools = []
        for i in range(0, 4):
            bools.append(self.floors[i] == other.floors[i])
        return all(bools)

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

    def is_solved(self):
        return self.floor(len(self.floors)).is_full()


class PuzzleSolver:

    def solve(self, building, i, move_list = []):
        move_list.append(building)
        i += -1
        if i < 0:
            return move_list
        else:
            next_moves = PuzzleSolver().possible_next_steps(building)
            for move in next_moves:
                PuzzleSolver().solve(move, i, move_list)

    def possible_next_steps(self, building):
        pel = self.possible_elevator_loads(building)
        elevator_moves = [self.possible_elevator_moves(ec) for ec in pel]
        return flatten(elevator_moves)

    def possible_elevator_loads(self, building):
        possible_combos = []
        # Elevators loads 0
        possible_combos.append(deepcopy(building))
        # Elevator loads 1
        floor = building.elevator_floor
        if floor.n_things() > 0:
            for thing in floor.non_lift_things():
                floor.load_elevator(thing)
                if floor.is_valid() and floor.elevator().is_valid():
                    possible_combos.append(deepcopy(building))
                floor.unload_elevator()
        if floor.n_things() > 1:
            combos = floor.thing_combos()
            for combo in combos:
                floor.load_elevator(combo[0])
                floor.load_elevator(combo[1])
                if floor.is_valid() and floor.elevator().is_valid():
                    possible_combos.append(deepcopy(building))
                floor.unload_elevator()
        return possible_combos

    def possible_elevator_moves(self, building):
        results = []
        # Move down
        if building.elevator_floor.number > 1:
            building_down = deepcopy(building)
            building_down.move_elevator(-1)
            building_down.elevator_floor.unload_elevator()
            if building_down.is_valid():
                results.append(building_down)
        if building.elevator_floor.number < 4:
            building_up = deepcopy(building)
            building_up.move_elevator(1)
            building_up.elevator_floor.unload_elevator()
            if building_up.is_valid():
                results.append(building_up)
        return results

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
    pz = PuzzleSolver()
