# --- Day 21: Scrambled Letters and Hash ---
#
# The computer system you're breaking into uses a weird scrambling function to 
# store its passwords. It shouldn't be much trouble to create your own 
# scrambled password so you can add it to the system; you just have to 
# implement the scrambler.
#
# The scrambling function is a series of operations (the exact list is provided
# in your puzzle input). Starting with the password to be scrambled, apply each
# operation in succession to the string. The individual operations behave as 
# follows:
#
# swap position X with position Y means that the letters at indexes X and Y 
# (counting from 0) should be swapped.
# swap letter X with letter Y means that the letters X and Y should be swapped 
# (regardless of where they appear in the string).
# rotate left/right X steps means that the whole string should be rotated; for 
# example, one right rotation would turn abcd into dabc.
# rotate based on position of letter X means that the whole string should be 
# rotated to the right based on the index of letter X (counting from 0) as 
# determined before this instruction does any rotations. Once the index is 
# determined, rotate the string to the right one time, plus a number of times 
# equal to that index, plus one additional time if the index was at least 4.
# reverse positions X through Y means that the span of letters at indexes X 
# through Y (including the letters at X and Y) should be reversed in order.
# move position X to position Y means that the letter which is at index X 
# should be removed from the string, then inserted such that it ends up at 
# index Y.
#
# For example, suppose you start with abcde and perform the following 
# operations:
#
# swap position 4 with position 0 swaps the first and last letters, producing 
# the input for the next step, ebcda.
# swap letter d with letter b swaps the positions of d and b: edcba.
# reverse positions 0 through 4 causes the entire string to be reversed, 
# producing abcde.
# rotate left 1 step shifts all letters left one position, causing the first 
# letter to wrap to the end of the string: bcdea.
# move position 1 to position 4 removes the letter at position 1 (c), then 
# inserts it at position 4 (the end of the string): bdeac.
# move position 3 to position 0 removes the letter at position 3 (a), then 
# inserts it at position 0 (the front of the string): abdec.
# rotate based on position of letter b finds the index of letter b (1), then 
# rotates the string right once plus a number of times equal to that index (2):
# ecabd.
# rotate based on position of letter d finds the index of letter d (4), then 
# rotates the string right once, plus a number of times equal to that index, 
# plus an additional time because the index was at least 4, for a total of 6 
# right rotations: decab.
# After these steps, the resulting scrambled password is decab.
#
# Now, you just need to generate a new scrambled password and you can access 
# the system. Given the list of scrambling operations in your puzzle input, 
# what is the result of scrambling abcdefgh?
#
# Your puzzle answer was hcdefbag.
#
# --- Part Two ---
#
# You scrambled the password correctly, but you discover that you can't 
# actually modify the password file on the system. You'll need to un-scramble 
# one of the existing passwords by reversing the scrambling process.
#
# What is the un-scrambled version of the scrambled password fbgdceah?
#
# ----------------------------------------------------------------------------

import re

class PasswordGenerator:

    def __init__(self, rules):
        self.rules = rules

    def __repr__(self):
        return self.pwd

    def scramble_password(self, pwd):
        self.pwd = pwd
        for rule in self.rules:
            self.parse_rule_scramble(rule)
        return self.pwd

    def unscramble_password(self, pwd):
        self.pwd = pwd
        for rule in reversed(self.rules):
            self.parse_rule_unscramble(rule)
        return self.pwd

    def parse_rule_scramble(self, rule):
        rules_regex = 'swap position|swap letter|reverse|rotate based|rotate|move'
        search = re.search(rules_regex, rule).group(0)
        if search == 'swap position':
            pos1 = int(re.search('[0-9]+', rule).group(0))
            pos2 = int(re.search('[0-9]+$', rule).group(0))
            return self.swap_position(pos1, pos2)
        elif search == 'swap letter':
            letter1 = re.search('(?<= )[a-z](?= )', rule).group(0)
            letter2 = re.search('(?<= )[a-z]$', rule).group(0)
            return self.swap_letter(letter1, letter2)
        elif search == 'reverse':
            pos1 = int(re.search('[0-9]+', rule).group(0))
            pos2 = int(re.search('[0-9]+$', rule).group(0))
            return self.reverse(pos1, pos2)
        elif search == 'rotate':
            direction = re.search('left|right', rule).group(0)
            steps = int(re.search('[0-9]+', rule).group(0))
            return self.rotate_direction(direction, steps)
        elif search == 'rotate based':
            letter = re.search('(?<= )[a-z]$', rule).group(0)
            return self.rotate_letter(letter)
        elif search == 'move':
            pos1 = int(re.search('[0-9]+', rule).group(0))
            pos2 = int(re.search('[0-9]+$', rule).group(0))
            return self.move(pos1, pos2)

    def parse_rule_unscramble(self, rule):
        rules_regex = 'swap position|swap letter|reverse|rotate based|rotate|move'
        search = re.search(rules_regex, rule).group(0)
        if search == 'swap position':
            pos1 = int(re.search('[0-9]+', rule).group(0))
            pos2 = int(re.search('[0-9]+$', rule).group(0))
            return self.swap_position(pos1, pos2)
        elif search == 'swap letter':
            letter1 = re.search('(?<= )[a-z](?= )', rule).group(0)
            letter2 = re.search('(?<= )[a-z]$', rule).group(0)
            return self.swap_letter(letter1, letter2)
        elif search == 'reverse':
            pos1 = int(re.search('[0-9]+', rule).group(0))
            pos2 = int(re.search('[0-9]+$', rule).group(0))
            return self.reverse(pos1, pos2)
        elif search == 'rotate':
            direction = re.search('left|right', rule).group(0)
            steps = int(re.search('[0-9]+', rule).group(0))
            if direction == 'left':
                direction = 'right'
            else:
                direction = 'left'
            return self.rotate_direction(direction, steps)
        elif search == 'rotate based':
            letter = re.search('(?<= )[a-z]$', rule).group(0)
            return self.unrotate_letter(letter)
        elif search == 'move':
            pos1 = int(re.search('[0-9]+', rule).group(0))
            pos2 = int(re.search('[0-9]+$', rule).group(0))
            return self.move(pos2, pos1)

    def swap_position(self, pos1, pos2):
        chars = list(self.pwd)
        char1 = chars[pos1]
        char2 = chars[pos2]
        chars[pos1] = char2
        chars[pos2] = char1
        self.pwd = ''.join(chars)
        return self.pwd

    def swap_letter(self, char1, char2):
        chars = list(self.pwd)
        index1 = chars.index(char1)
        index2 = chars.index(char2)
        chars[index1] = char2
        chars[index2] = char1
        self.pwd = ''.join(chars)
        return self.pwd

    def reverse(self, pos1, pos2):
        chars = list(self.pwd)
        before = chars[:pos1]
        rev = list(reversed(chars[pos1:pos2+1]))
        after = chars[pos2+1:]
        self.pwd = ''.join(before + rev + after)
        return self.pwd

    def rotate_direction(self, direction, steps):
        chars = list(self.pwd)
        if direction == 'right':
            sign = -1
        elif direction == 'left':
            sign = 1
        indicies = [(i + steps*sign) % len(chars) for i in range(len(chars))]
        self.pwd = ''.join([chars[i] for i in indicies])
        return self.pwd

    def rotate_letter(self, letter):
        index = self.pwd.index(letter)
        if index >= 4:
            extra = 1
        else:
            extra = 0
        return self.rotate_direction('right', 1 + index + extra)

    def unrotate_letter(self, letter):
        len_ = len(self.pwd)
        index = self.pwd.index(letter)
        if index == 1:
            return self.rotate_direction('left', 1)
        if index == 3:
            return self.rotate_direction('left', 2)
        if index == 5:
            return self.rotate_direction('left', 3)
        if index == 7:
            return self.rotate_direction('left', 4)
        if index == 2:
            return self.rotate_direction('left', 6)
        if index == 4:
            return self.rotate_direction('left', 7)
        if index == 6:
            return self.rotate_direction('left', 8)
        if index == 0:
            return self.rotate_direction('left', 9)

    def move(self, pos1, pos2):
        chars = list(self.pwd)
        char1 = chars[pos1]
        chars.remove(char1)
        chars.insert(pos2, char1)
        self.pwd = ''.join(chars)
        return self.pwd

if __name__ == '__main__':
    test_rules = open('inputs/day21_test.txt').read().splitlines()
    test_pg = PasswordGenerator(test_rules)
    assert(test_pg.scramble_password('abcde') == 'decab')
    
    rules = open('inputs/day21.txt').read().splitlines()
    pg = PasswordGenerator(rules)
    print('Part 1:', pg.scramble_password('abcdefgh'))
    
    assert(pg.unscramble_password('hcdefbag') == 'abcdefgh')
    print('Part 2:', pg.unscramble_password('fbgdceah'))
