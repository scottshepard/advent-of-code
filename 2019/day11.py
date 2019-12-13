from utils import read_input
from intcode import IntcodeComputer
import copy

class HullPaintingRobot:

    def __init__(self, input):
        self.input_raw = copy.deepcopy(input)
        self.brain = IntcodeComputer(input)
        self.direction = 'UP'
        self.hull = {}
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
robot = HullPaintingRobot(input)

while not robot.solved:
    robot.next()

print("Solutio to Day 11 Part I is {}".format(len(list(robot.hull.values()))))
