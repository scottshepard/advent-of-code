from utils import read_input
from intcode import IntcodeComputer
import copy

import numpy as np
from matplotlib import pyplot as plt

class HullPaintingRobot:

    def __init__(self, input, starting_panel):
        self.input_raw = copy.deepcopy(input)
        self.brain = IntcodeComputer(input)
        self.direction = 'UP'
        self.hull = {(0, 0): starting_panel}
        self.x = 0
        self.y = 0
        self.solved = False

    def next(self):
        self.paint_and_turn()
        self.move()

    def get_color(self, coord):
        if coord in self.hull.keys():
            return self.hull[coord]
        else:
            return 0

    def paint_and_turn(self):
        output, solved = self.brain.next([self.get_color((self.x, self.y))])
        self.solved = solved
        color = output[0]
        self.hull[(self.x, self.y)] = color
        turn_int = output[1]
        self.direction = self.turn(self.direction, turn_int)

    def turn(self, direction, int):
        assert int in [0,1]
        assert direction in ['UP','DN','LT','RT']
        if direction == 'UP':
            if int == 1:
                return 'RT'
            elif int == 0:
                return 'LT'
        elif direction == 'DN':
            if int == 1:
                return 'LT'
            elif int == 0:
                return 'RT'
        elif direction == 'LT':
            if int == 1:
                return 'UP'
            elif int == 0:
                return 'DN'
        elif direction == 'RT':
            if int == 1:
                return 'DN'
            elif int == 0:
                return 'UP'

    def move(self):
        if self.direction == 'UP':
            self.y += 1
        elif self.direction == 'DN':
            self.y -= 1
        elif self.direction == 'LT':
            self.x -= 1
        elif self.direction == 'RT':
            self.x += 1


input = read_input('day11.txt')[0]

robot = HullPaintingRobot(input, starting_panel = 0)
while not robot.solved:
    robot.next()

print("Solutiom to Day 11 Part I is {}".format(len(list(robot.hull.values()))))

robot = HullPaintingRobot(input, starting_panel = 1)exi
while not robot.solved:
    robot.next()

# Write output imge
x_s = [k[0] for k in robot.hull.keys()]
y_s = [k[1] for k in robot.hull.keys()]
min_y = min(y_s)
min_x = min(x_s)

hull_shape = (max(y_s) - min(y_s) + 1, max(x_s) - min(x_s) + 1)
arr = np.zeros(hull_shape)

for k, v in robot.hull.items():
    arr[k[1] - min_y][k[0] - min_x] = v
arr = np.flip(arr, 0)
plt.imshow(arr, interpolation='nearest')
plt.savefig('day11_part2.png')
print('Solution to Day 11 Part II is in day11_part2.png')
