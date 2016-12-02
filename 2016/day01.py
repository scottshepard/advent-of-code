import re

f = open('data.txt', 'r')
data = f.read()

class Location:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cardinal = 'North'
        self.next_move = None
        self.previous_locations = []
    
    def current_location(self):
        return (self.x, self.y)

    def parse_move(self, string):
        direction = re.search('R|L', string).group(0)
        distance = int(re.search('[0-9]+', string).group(0))
        self.next_move = (direction, distance)
        return self.next_move

    def move(self, direction=None, distance=None):
        if(direction is None):
            direction = self.next_move[0]
        if(distance is None):
            distance = self.next_move[1]
        self.turn(direction)
        for i in range(distance):
            self.move1(self.cardinal)
        self.next_move = None
        return (self.current_location())

    def move1(self, cardinal):
        self.previous_locations.append(self.current_location())
        if(cardinal == 'North'):
            self.y = self.y + 1
        elif(cardinal == 'South'):
            self.y = self.y - 1
        elif(cardinal == 'East'):
            self.x = self.x + 1
        elif(cardinal == 'West'):
            self.x = self.x - 1
        
    def turn(self, direction):
        cardinal = self.cardinal
        if(cardinal == 'North'):
            if(direction == 'R'):
               cardinal = 'East'
            elif(direction == 'L'):
                cardinal = 'West'
        elif(cardinal == 'South'):
            if(direction == 'R'): 
                cardinal = 'West'
            elif(direction == 'L'):
                cardinal = 'East'
        elif(cardinal == 'East'):
            if(direction == 'R'):
                cardinal = 'South'
            elif(direction == 'L'):
                cardinal = 'North'
        elif(cardinal == 'West'):
            if(direction == 'R'):
                cardinal = 'North'
            elif(direction == 'L'):
                cardinal = 'South'
        self.cardinal = cardinal
        return self.cardinal

if __name__ == '__main__':
    f = open('data.txt')
    data = f.read()
    moves = re.split(',', data)
    bunny = Location()

    # Part 1, go through all the moves
    for move in moves:
        bunny.parse_move(move)
        bunny.move()
    print(abs(bunny.x) + abs(bunny.y))

    # Part 2, find first overlapping location
    for i in reversed(range(len(bunny.previous_locations))):
        if(bunny.previous_locations[i] in bunny.previous_locations[0:(i-1)]):
            print(True)
        print(bunny.previous_locations[i])
