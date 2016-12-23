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
