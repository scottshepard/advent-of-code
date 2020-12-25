from utils import read_input


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round = 0

    def __next__(self):
        p1_card = self.p1.pop(0)
        p2_card = self.p2.pop(0)
        if p1_card > p2_card:
            self.p1.extend([p1_card, p2_card])
        else:
            self.p2.extend([p2_card, p1_card])
        self.round += 1

    def __repr__(self):
        return 'P1: ' + str(self.p1) + '\nP2: ' + str(self.p2)

    def solve(self):
        while len(self.p1) > 0 and len(self.p2) > 0:
            self.__next__()
        return self.score()

    def score(self):
        if len(self.p1) == 0:
            x = self.p2
        else:
            x = self.p1
        return sum([(i+1) * int(c) for i, c in enumerate(x[::-1])])

def parse_input(input):
    lines = read_input(input, '\n\n')
    players = []
    for l in lines:
        x = l.split('\n')
        x.pop(0)
        players.append([int(i) for i in x])
    return players

p1, p2 = parse_input('day22_test.txt')
g = Game(p1, p2)
g.solve() == 306

p1, p2 = parse_input('day22.txt')
g = Game(p1, p2)
print('Part 1:', g.solve())
