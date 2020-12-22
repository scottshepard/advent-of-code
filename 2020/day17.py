from utils import read_input

class Game:

    def __init__(self, input):
        self.min_z = -1
        self.max_z = 1
        self.min_x = -1
        self.max_x = len(input[0])
        self.min_y = -1
        self.max_y = len(input)
        grid = {}
        legend = {
            '.': 0,
            '#': 1
        }
        for y in range(len(input)):
            for x in range(len(input[0])):
                grid[(x,y,0)] = legend[input[y][x]]
        self.grid = grid

    def cycle(self, n_cycles):
        for n in range(n_cycles):
            grid = {}
            for x in range(self.min_x, self.max_x+1):
                for y in range(self.min_y, self.max_y+1):
                    for z in range(self.min_z, self.max_z+1):
                        grid[(x, y, z)] = self._cycle_cube(x, y, z)
            self.min_x -= 1
            self.min_y -= 1
            self.min_z -= 1
            self.max_x += 1
            self.max_y += 1
            self.max_z += 1
            self.grid = grid

    def _cycle_cube(self, x, y, z):
        n_active = self._check_neighbors(x, y, z)
        if (x, y, z) in self.grid:
            current = self.grid[(x, y, z)]
        else:
            current = 0
        if current == 1:
            if n_active in (2, 3):
                next = 1
            else:
                next = 0
        elif current == 0:
            if n_active == 3:
                next = 1
            else:
                next = 0
        else:
            raise
        return next

    def _check_neighbors(self, x, y, z):
        n_active = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if i == j == k == 0:
                        pass
                    elif (x+i, y+j, z+k) in self.grid:
                        n_active += self.grid[(x+i, y+j, z+k)]
        return n_active

class Game2:

    def __init__(self, input):
        self.min_z = -1
        self.max_z = 1
        self.min_x = -1
        self.max_x = len(input[0])
        self.min_y = -1
        self.max_y = len(input)
        self.min_w = -1
        self.max_w = 1
        self.grid = {}
        legend = {
            '.': 0,
            '#': 1
        }
        for y in range(len(input)):
            for x in range(len(input[0])):
                self.grid[(x,y,0,0)] = legend[input[y][x]]

    def cycle(self, n_cycles):
        for n in range(n_cycles):
            grid = {}
            for w in range(self.min_w, self.max_w+1):
                for x in range(self.min_x, self.max_x+1):
                    for y in range(self.min_y, self.max_y+1):
                        for z in range(self.min_z, self.max_z+1):
                            grid[(x, y, z, w)] = self._cycle_cube(x, y, z, w)
            self.min_x -= 1
            self.min_y -= 1
            self.min_z -= 1
            self.min_w -= 1
            self.max_x += 1
            self.max_y += 1
            self.max_z += 1
            self.max_w += 1
            self.grid = grid

    def _cycle_cube(self, x, y, z, w):
        n_active = self._check_neighbors(x, y, z, w)
        if (x, y, z, w) in self.grid:
            current = self.grid[(x, y, z, w)]
        else:
            current = 0
        if current == 1:
            if n_active in (2, 3):
                next = 1
            else:
                next = 0
        elif current == 0:
            if n_active == 3:
                next = 1
            else:
                next = 0
        else:
            raise
        return next

    def _check_neighbors(self, x, y, z, w):
        n_active = 0
        for l in range(-1, 2):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        if i == j == k == l == 0:
                            pass
                        elif (x+i, y+j, z+k, w+l) in self.grid:
                            n_active += self.grid[(x+i, y+j, z+k, w+l)]
        return n_active


sample_input = read_input('day17_test.txt')
g = Game(sample_input)
g.cycle(6)
assert sum(g.grid.values()) == 112

real_input = read_input('day17.txt')
g = Game(real_input)
g.cycle(6)
print('Part 1:', sum(g.grid.values()))

g2 = Game2(sample_input)
g2.cycle(6)
assert sum(g2.grid.values()) == 848

g2 = Game2(real_input)
g2.cycle(6)
print('Part 2:', sum(g2.grid.values()))
