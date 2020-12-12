from utils import read_input
import pdb


class GameOfLife:

    def __init__(self, input, mode):
        self.map = input
        self.mode = mode

    def _next_state_1(self, x, y):
        n_occupied = 0
        n_empty = 0
        for i in range(x-1, x+2):
            if (i < 0) or (i == len(self.map[0])):
                continue
            for j in range(y-1, y+2):
                if (x == i) and (j == y):
                    continue
                if (j < 0) or (j == len(self.map)):
                    continue
                if self.map[j][i] == '#':
                    n_occupied += 1
                elif self.map[j][i] == 'L':
                    n_empty += 1

        result = self.map[y][x]
        if self.map[y][x] == '.':
            pass
        elif self.map[y][x] == 'L':
            if n_occupied == 0:
                result = '#'
        elif self.map[y][x] == '#':
            if n_occupied >= 4:
                result = 'L'
        return result

    def __next__(self):
        self.previous_map = self.map
        new_map = []
        for j in range(len(self.map)):
            new_row = []
            for i in range(len(self.map[0])):
                if self.mode == 1:
                    new_row.append(self._next_state_1(i, j))
                elif self.mode == 2:
                    new_row.append(self._next_state_2(i, j))
            new_map.append(''.join(new_row))
        self.map = new_map
        return self.map

    def _count_occupied_seats(self):
        seats = ''.join(self.map)
        return sum([x == '#' for x in seats])

    def solve(self):
        next(self)
        while self.previous_map != self.map:
            next(self)
        return self._count_occupied_seats()



sample_input = read_input('day11_test.txt')
g = GameOfLife(sample_input)
assert g.solve() == 37

real_input = read_input('day11.txt', 1)
g = GameOfLife(real_input)
print('Part 1:', g.solve())
