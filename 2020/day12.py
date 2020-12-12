from utils import read_input
import numpy as np


class Ship:

    def __init__(self, mode):
        self.mode = mode
        self.x = 0
        self.y = 0
        self.dir = 0
        self.wp_x = 10
        self.wp_y = 1

    def __repr__(self):
        return str((self.x, self.y))

    def navigate(self, instructions):
        for instr in instructions:
            self._move_once(instr)
        return self.x, self.y

    def _move_once(self, instr):
        action = instr[0]
        value = int(instr[1:])
        if self.mode == 1:
            if action == 'N':
                self.y += value
            elif action == 'S':
                self.y -= value
            elif action == 'E':
                self.x += value
            elif action == 'W':
                self.x -= value
            elif action in ['L', 'R']:
                self._turn_ship(action, value)
            elif action == 'F':
                if self.dir == 0:
                    self.x += value
                elif self.dir == 90:
                    self.y += value
                elif self.dir == 180:
                    self.x -= value
                elif self.dir == 270:
                    self.y -= value
        elif self.mode == 2:
            if action == 'N':
                self.wp_y += value
            elif action == 'S':
                self.wp_y -= value
            elif action == 'E':
                self.wp_x += value
            elif action == 'W':
                self.wp_x -= value
            elif action in ['L', 'R']:
                self._rotate_waypoint(action, value)
            elif action == 'F':
                self.x += self.wp_x * value
                self.y += self.wp_y * value

    def _turn_ship(self, dir, val):
        dir_map = {'L': 1, 'R': -1}
        self.dir = (self.dir + (val * dir_map[dir])) % 360
        while self.dir < 0:
            self.dir += 360
        return self.dir

    def _rotate_waypoint(self, dir, val):
        '''
        Use a rotation matrix to transform the waypoint vector.
        Needs to be converted back to int to account for small rounding errors
        '''
        dir_map = {'L': 1, 'R': -1}
        theta = np.radians((val * dir_map[dir]) % 360)
        r = np.array(((np.cos(theta), -np.sin(theta)),
                      (np.sin(theta), np.cos(theta))))
        wp_x, wp_y = r.dot(np.array([self.wp_x, self.wp_y]))
        self.wp_x, self.wp_y = int(np.round(wp_x)), int(np.round(wp_y))
        return self.wp_x, self.wp_y


def manhattan_distance(pos):
    return abs(pos[0]) + abs(pos[1])

def solve(input, mode):
    s = Ship(mode)
    pos = s.navigate(input)
    return manhattan_distance(pos)


sample_input = read_input('day12_test.txt')
assert solve(sample_input, 1) == 25
real_input = read_input('day12.txt')
print('Part 1:', solve(real_input, 1))

assert solve(sample_input, 2) == 286
print('Part 2:', solve(real_input, 2))
