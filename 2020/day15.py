

class Game:

    def __init__(self, input):
        self.turn = len(input)
        self.next_num = input[-1]
        input.pop()
        self.dict = {}
        for i, n in enumerate(input):
            self.dict[n] = i+1

    def __next__(self):
        last_played = self.dict.get(self.next_num)
        self.dict[self.next_num] = self.turn
        if last_played is None:
            next_num = 0
        else:
            next_num = self.turn - last_played
        self.turn += 1
        self.next_num = next_num
        return next_num

    def play(self, n):
        while self.turn < n:
            x = next(self)
        return x


g = Game([0, 3, 6])
assert g.play(10) == 0
assert g.play(2020) == 436

g = Game([13,16,0,12,15,1])
print('Part 1:', g.play(2020))
print('Part 2:', g.play(30000000))
