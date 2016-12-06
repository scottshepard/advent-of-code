# --- Day 12: JSAbacusFramework.io ---
#
# Santa's Accounting-Elves need help balancing the books after a recent order. 
# Unfortunately, their accounting software uses a peculiar storage format. 
# That's where you come in.
#
# They have a JSON document which contains a variety of things: 
# arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. 
# Your first job is to simply find all of the numbers throughout the document 
# and add them together.
#
# For example:
#
# [1,2,3] and {"a":2,"b":4} both have a sum of 6.
# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
# [] and {} both have a sum of 0.
# You will not encounter any strings containing numbers.
#
# What is the sum of all numbers in the document?
#
# --- Part Two ---
#
# Uh oh - the Accounting-Elves have realized that they double-counted
# everything red.
#
# Ignore any object (and all of its children) which has any property with the 
# value "red". Do this only for objects ({...}), not arrays ([...]).
#
# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, 
# because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, 
# because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.
# 
# -----------------------------------------------------------------------------

import json
import re

class Day12:

    def __init__(self, data):
        self.data = data
        self.json = json.loads(data)
        self.no_red_sum = 0

    def sum_all_numbers(self):
        numbers = re.findall('-?[0-9]*', self.data)
        return sum([int(n) for n in numbers if n != ''])

    def sum_nonred(self, json):
        # Base case
        if(type(json) is int):
            return json
        elif(type(json) is str):
            return 0
        # If list, iterate through list and get the sum 
        # of each item protecting for None
        elif(type(json) is list):
            result = 0
            for item in json:
                summand = self.sum_nonred(item)
                if(summand is not None):
                    result += summand
            return result
        # If dict, check first for a 'red' value, if
        # not pass back into recurrsion and let 
        # the list step handle it
        elif(type(json) is dict):
            values = list(json.values())
            if('red' in values):
                return 0
            else:
                return self.sum_nonred(values)

if __name__ == '__main__':
    fileobject = open('day12.txt', 'r')
    data = fileobject.read()

    day12 = Day12(data)

    print("Part 1:", day12.sum_all_numbers())
    # Correct answer is 191164

    print("Part 2:", day12.sum_nonred(day12.json))
    # Correct answer is 87842
