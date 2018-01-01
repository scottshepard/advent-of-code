import re
import os
from string import ascii_lowercase

class Dance:

    def __init__(self, n, moves):
        self.n = n
        self.moves = moves
        self.programs = list(ascii_lowercase)[:n]
        self.end_states = []

    def __str__(self):
        return ''.join(self.programs)

    def __repr__(self):
        return str(self)

    def solve_n_times(self, n):
        for i in range(n):
            if str(self) in self.end_states:
                return self.end_states[n % len(self.end_states)]
            else:
                self.solve()
        return str(self)

    def solve(self):
        self.end_states.append(str(self))
        for m in self.moves:
            self.parse_move(m)
        return str(self)

    def parse_move(self, move):
        inst = move[0]
        if inst == 's':
            return self.spin(int(move[1:]))
        if inst == 'x':
            ab = re.findall('[0-9]+', move[1:])
            return self.exchange(int(ab[0]), int(ab[1]))
        if inst == 'p':
            ab = re.findall('[a-z]+', move[1:])
            return self.partner(ab[0], ab[1])

    def spin(self, X):
        progs = self.programs
        self.programs = progs[len(progs)-X:] + progs[:len(progs)-X]
        return str(self)

    def exchange(self, A, B):
        p1 = self.programs[A]
        p2 = self.programs[B]
        self.programs[A] = p2
        self.programs[B] = p1
        return str(self)

    def partner(self, A, B):
        a_i = self.programs.index(A)
        b_i = self.programs.index(B)
        self.programs[a_i] = B
        self.programs[b_i] = A
        return str(self)

if __name__ == '__main__':
    rel_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(rel_path, "inputs/day16_test.txt")
    test_moves = open(file_path).read().split(',')
    d1 = Dance(5, test_moves)
    print(d1.solve())

    rel_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(rel_path, "inputs/day16.txt")
    moves = open(file_path).read().split(',')
    d2 = Dance(16, moves)
    print(d2.solve())
    print(d2.solve_n_times(1000000000))
