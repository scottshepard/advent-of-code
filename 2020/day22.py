from utils import read_input


class Game:

    def __init__(self, p1, p2, mode='normal'):
        self.p1 = p1.copy()
        self.p2 = p2.copy()
        self.round = 0
        self.mode = mode
        self.configurations = []
        self.solved = False

    def __next__(self):
        if (self.p1, self.p2) in self.configurations:
            self.solved = True
            self.winner = 1
        else:
            self.configurations.append((self.p1.copy(), self.p2.copy()))
            p1_card = self.p1.pop(0)
            p2_card = self.p2.pop(0)

            winner = self._determine_winner(p1_card, p2_card)

            if winner == 1:
                self.p1.extend([p1_card, p2_card])
            else:
                self.p2.extend([p2_card, p1_card])
            if len(self.p1) == 0:
                self.solved = True
                self.winner = 2
            if len(self.p2) == 0:
                self.solved = True
                self.winner = 1
            self.round += 1

    def _determine_winner(self, p1_card, p2_card):
        if (p1_card <= len(self.p1)) and (p2_card <= len(self.p2)) and (self.mode == 'recursive'):
            g = Game(self.p1[:p1_card], self.p2[:p2_card], 'recursive')
            winner, _ = g.play()
        else:
            if p1_card > p2_card:
                winner = 1
            elif p2_card > p1_card:
                winner = 2
        return winner

    def __repr__(self):
        return 'P1: ' + str(self.p1) + '\nP2: ' + str(self.p2)

    def play(self):
        while not self.solved:
            self.__next__()
        return self.winner, self.score()

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
assert g.play() == (2, 306)

g2 = Game(p1, p2, mode='recursive')
assert g2.play() == (2, 291)

p1, p2 = parse_input('day22.txt')
g = Game(p1, p2)
_, score = g.play()
print('Part 1:', score)

p1, p2 = parse_input('day22.txt')
g2 = Game(p1, p2, mode='recursive')
_, score = g2.play()
print('Part 2:', score)
