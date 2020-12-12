from utils import read_input
import pdb


class GameOfLife:

    def __init__(self, input, mode):
        self.map = input
        self.mode = mode

    def __next__(self):
        self.previous_map = self.map
        new_map = []
        for j in range(len(self.map)):
            new_row = []
            for i in range(len(self.map[0])):
                new_row.append(self._next_state(i, j))
            new_map.append(''.join(new_row))
        self.map = new_map
        return self.map

    def _next_state(self, x, y):
        n_occupied = self._count_adjacent_occupied_seats(x, y)
        if (self.map[y][x] == 'L') and (n_occupied==0):
            result = '#'
        elif (self.map[y][x] == '#') and ((n_occupied>=4 and self.mode==1) or (n_occupied>=5 and self.mode==2)):
            result = 'L'
        else:
            result = self.map[y][x]
        return result

    def _count_adjacent_occupied_seats(self, x, y):
        n_occupied = 0
        if self.mode == 1:
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
        elif self.mode == 2:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    seat = self._first_seat(x, y, i, j)
                    if seat is not None:
                        if self.map[seat[1]][seat[0]] == '#':
                            n_occupied += 1
        return n_occupied

    def _first_seat(self, x, y, x_dir, y_dir):
        if (x_dir == 0) and (y_dir == 0):
            return
        x += x_dir
        y += y_dir
        if (x < 0) or (x == len(self.map[0])) or (y < 0) or (y == len(self.map)):
            return
        while (self.map[y][x] == '.'):
            x += x_dir
            y += y_dir
            if (x < 0) or (x == len(self.map[0])) or (y < 0) or (y == len(self.map)):
                return
        return x, y

    def _count_total_occupied_seats(self):
        seats = ''.join(self.map)
        return sum([x == '#' for x in seats])

    def solve(self):
        next(self)
        while self.previous_map != self.map:
            next(self)
        return self._count_total_occupied_seats()



sample_input = read_input('day11_test.txt')
g = GameOfLife(sample_input, 1)
assert g.solve() == 37

g = GameOfLife(sample_input, 2)
assert g.solve() == 26

real_input = read_input('day11.txt')
g1 = GameOfLife(real_input, 1)
print('Part 1:', g1.solve())

g2 = GameOfLife(real_input, 2)
print('Part 2:', g2.solve())

