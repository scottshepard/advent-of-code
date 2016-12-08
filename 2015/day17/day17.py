# --- Day 17: No Such Thing as Too Much ---
#
# The elves bought too much eggnog again - 150 liters this time. To fit it all 
# into your refrigerator, you'll need to move it into smaller containers. 
# You take an inventory of the capacities of the available containers.
#
# For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters.
# If you need to store 25 liters, there are four ways to do it:
#
# 15 and 10
# 20 and 5 (the first 5)
# 20 and 5 (the second 5)
# 15, 5, and 5
#
# Filling all containers entirely, how many different combinations of 
# containers can exactly fit all 150 liters of eggnog?
#
# --- Part Two ---
#
# While playing with all the containers in the kitchen, another load of eggnog 
# arrives! The shipping and receiving department is requesting as many 
# containers as you can spare.
#
# Find the minimum number of containers that can exactly fit all 150 liters of 
# eggnog. How many different ways can you fill that number of containers and 
# still hold exactly 150 litres?
#
# In the example above, the minimum number of containers was two. 
# There were three ways to use that many containers, and so the answer there 
# would be 3.
#
# -----------------------------------------------------------------------------

from itertools import combinations
import re

if __name__ == '__main__':
    target = 150

    fileobject = open('day17.txt')
    data = fileobject.read()
    containers = [int(x) for x in re.split('\n', data)]
    bools = []
    lens = []
    for i in range(len(containers)):
        combos = combinations(containers, i+1)
        for combo in combos:
            bools.append(sum(combo) == 150)
            lens.append(len(combo))

    print("Part 1:", sum(bools))
    # Correct answer is 1638

    print("Part 2:", len([b for n, b in zip(lens, bools) if b and n == 4]))
    # Correct answer is 17
