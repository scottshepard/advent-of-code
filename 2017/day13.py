import os

class Firewall:
    def __init__(self, layers):
        self.layers = []
        self.parse(layers)
        self.hacker = 0
        self.severity = 0
        self.layers[self.hacker].hacker = True

    def __iter__(self):
        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.layers)

    def parse(self, layers):
        for layer in layers:
            d, r = layer.split(':')
            self.layers.append(Layer(int(d), int(r)))
        return self.layers

    def next(self):
        for layer in self.layers:
            self.severity += next(layer)
        self.layers[self.hacker].hacker = False
        self.hacker += 1
        if self.hacker < len(self.layers):
            self.layers[self.hacker].hacker = True
        return self

    def solve(self):
        for i in range(0, len(self.layers)):
            next(self)
        return self.severity

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

    def next(self):
        severity = self.severity()
        self.scanner += self.direction
        if (self.scanner == self.range-1) or (self.scanner == 0):
            self.direction = -self.direction
        return severity

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
    print(fw.solve())
