import re
from utils import read_input


class Deck:

    def __init__(self, n_cards):
        self.n_cards = n_cards
        self.factory_reset()

    def factory_reset(self):
        self.cards = [i for i in range(self.n_cards)]

    def deal_into_stack(self):
        self.cards.reverse()
        return self.cards

    def cut(self, n):
        x = self.cards[n:]
        y = self.cards[:n]
        self.cards = x + y
        return self.cards

    def deal_with_increment(self, n):
        new_stack = [i for i in range(self.n_cards)]
        i = 0
        while len(self.cards) > 0:
            i = i % self.n_cards
            new_stack[i] = self.cards.pop(0)
            i += n
        self.cards = new_stack
        return self.cards


class Game:

    def __init__(self, instructions, N):
        self.instructions = instructions
        self.N = N
        self.deck = Deck(N)

    def parse_instruction(self, instruction):
        if instruction == 'deal into new stack':
            self.deck.deal_into_stack()
        elif 'deal with increment' in instruction:
            s = re.search('[0-9]+', instruction)
            n = int(s.group(0))
            self.deck.deal_with_increment(n)
        elif 'cut' in instruction:
            s = re.search('-?[0-9]+', instruction)
            n = int(s.group(0))
            self.deck.cut(n)

    def solve(self):
        for instruction in self.instructions:
            self.parse_instruction(instruction)
        return self.deck.cards


d = Deck(10)
assert d.deal_into_stack() == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
d.factory_reset()
assert d.cut(3) == [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
d.factory_reset()
assert d.cut(-4) == [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
d.factory_reset()
d.deal_with_increment(3) == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]

test_inputs = read_input('day22_test.txt')

g1 = Game(test_inputs[:3], 10)
assert g1.solve() == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]

g2 = Game(test_inputs[4:7], 10)
assert g2.solve() == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]

g3 = Game(test_inputs[8:11], 10)
assert g3.solve() == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]

g4 = Game(test_inputs[12:], 10)
assert g4.solve() == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]

input = read_input('day22.txt')
g = Game(input, 10007)
g.solve()
print('Solution to Day 22 Part I is {}'.format(g.deck.cards.index(2019)))
