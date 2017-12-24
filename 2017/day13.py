import os
from copy import deepcopy

class FirewallSolver:

    def __init__(self, layers):
        self.layers = layers
        self.picoseconds = 0
        self.firewall = Firewall(self.layers, self.picoseconds)
        self.solved = False

    def __iter__(self):
        return self

    def __next__(self):
        firewall = self.firewall
        fw_delayed = deepcopy(firewall)
        fw_delayed.delay(1)
        firewall.set_hacker()
        caught = firewall.caught()
        if caught:
            self.picoseconds += 1
            self.firewall = fw_delayed
            return self
        else:
            self.solved = True
            return self

    def delay(self, n):
        self.picoseconds += n
        self.firewall.delay(n)
        return 'Delayed ' + str(n) + ' steps'

    def solve(self):
        while not self.solved:
            next(self)
            if self.picoseconds % 1000 == 0:
                print(self.picoseconds)
        return self.picoseconds

class Firewall:
    def __init__(self, layers, delayed = 0):
        self.layers = []
        self.parse(layers)
        self.hacker = False
        self.severity = 0
        self.delay(delayed)

    def __iter__(self):
        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.layers)

    def __next__(self):
        for layer in self.layers:
            self.severity += next(layer)
        if self.hacker:
            self.layers[self.h_index].hacker = False
            self.h_index += 1
            if self.h_index < len(self.layers):
                self.layers[self.h_index].hacker = True
        return self

    def caught(self):
        for i in range(0, len(self.layers)):
            if self.currently_caught():
                return True
            else:
                next(self)
        return False

    def currently_caught(self):
        return any([l.caught() for l in self.layers])

    def set_hacker(self):
        self.hacker = True
        self.h_index = 0
        self.layers[self.h_index].hacker = True

    def parse(self, layers):
        for layer in layers:
            d, r = layer.split(':')
            self.layers.append(Layer(int(d), int(r)))
        return self.layers

    def compute_severity(self):
        for i in range(0, len(self.layers)):
            next(self)
        return self.severity

    def delay(self, delayed):
        while delayed > 0:
            next(self)
            delayed -= 1
        return self

class Layer:
    def __init__(self, depth, rnge):
        self.depth = depth
        self.range = rnge
        self.scanner = 0
        self.direction = 1
        self.empty = (self.range == 1)
        self.hacker = False

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.empty:
            if self.hacker:
                return str(['X'])
            else:
                return str([])
        else:
            arr = [[] for i in range(0, self.range)]
            arr[self.scanner] = ['S']
            if self.hacker:
                arr[0].append('X')
            return str(arr)

    def __iter__(self):
        return self

    def __next__(self):
        severity = self.severity()
        self.scanner += self.direction
        if (self.scanner == self.range-1) or (self.scanner == 0):
            self.direction = -self.direction
        return severity

    def caught(self):
        return self.hacker and self.scanner == 0

    def severity(self):
        if self.hacker and self.scanner == 0 and self.range > 1:
            return self.depth * self.range
        else:
            return 0

    
if __name__ == '__main__':    
    rel_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(rel_path, "inputs/day13.txt")
    f = open(file_path)
    data = f.read().split('\n')
    fw = Firewall(data)
    fw.set_hacker()
    print(fw.compute_severity())
    solver = FirewallSolver(data)
    solver.delay(3060000)
    print(solver.solve())
