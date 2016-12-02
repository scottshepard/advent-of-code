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
        self.previous_locations.append(self.current_location())
        if(direction is None):
            direction = self.next_move[0]
        if(distance is None):
            distance = self.next_move[1]
        self.turn(direction)
        cardinal = self.cardinal
        if(cardinal == 'North'):
            self.y = self.y + distance
        elif(cardinal == 'South'):
            self.y = self.y - distance
        elif(cardinal == 'East'):
            self.x = self.x + distance
        elif(cardinal == 'West'):
            self.x = self.x - distance
        self.next_move = None
        return (self.current_location())
        
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
    for move in moves:
        if(bunny.current_location() in bunny.previous_locations):
            print(True)
        bunny.parse_move(move)
        print(bunny.move())
    print(abs(bunny.x) + abs(bunny.y))

