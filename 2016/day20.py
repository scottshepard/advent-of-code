# --- Day 20: Firewall Rules ---
#
# You'd like to set up a small hidden computer here so you can use it to get 
# back into the network later. However, the corporate firewall only allows 
# communication with certain external IP addresses.
#
# You've retrieved the list of blocked IPs from the firewall, but the list 
# seems to be messy and poorly maintained, and it's not clear which IPs are 
# allowed. Also, rather than being written in dot-decimal notation, they are 
# written as plain 32-bit integers, which can have any value from 0 through 
# 4294967295, inclusive.
#
# For example, suppose only the values 0 through 9 were valid, and that you 
# retrieved the following blacklist:
#
# 5-8
# 0-2
# 4-7
#
# The blacklist specifies ranges of IPs (inclusive of both the start and end 
# value) that are not allowed. Then, the only IPs that this firewall allows are
# 3 and 9, since those are the only numbers not in any range.
#
# Given the list of blocked IPs you retrieved from the firewall (your puzzle 
# input), what is the lowest-valued IP that is not blocked?
#
# ----------------------------------------------------------------------------

import re

class Day20:

    def __init__(self, ips):
        self.ips = ips
        self.ranges = [self.parse_line(ip) for ip in ips]

    def parse_line(self, line):
        numbers = re.findall('[0-9]+', line)
        num0 = int(numbers[0])
        num1 = int(numbers[1])
        return range(num0, num1+1)

    def is_blacklisted(self, number):
        return any([number in range_ for range_ in self.ranges])

    def max_range(self, number):
        '''Finds the upper bound of the first range containing number'''
        for range_ in self.ranges:
            if number in range_:
                return range_[-1]

    def find_smallest(self, number=0):
        if self.is_blacklisted(number):
            new_number = self.max_range(number) + 1
            return self.find_smallest(new_number)
        else:
            return number

    def whitelist(self, number=0, whitelist=None):
        if whitelist is None:
            whitelist = []
        if number > 4294967295:
            return [ip for ip in whitelist if ip <= 4294967295]
        else:
            new_number = self.find_smallest(number)
            whitelist.append(new_number)
            return self.whitelist(new_number+1, whitelist)
        
if __name__ == '__main__':
    ips = open('inputs/day20.txt').read().splitlines()
    print('Part 1:', Day20(ips).find_smallest())
    print('Part 2:', len(Day20(ips).whitelist()))
