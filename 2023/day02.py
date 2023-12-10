from utils import read_input
import re
import pdb

games = read_input('day02.txt')



# Part 1

limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

valid_games = []
powers = []

for game in games:
    id, sets = game.split(':')
    id = int(re.search('[0-9]+', id).group(0))
    sets = sets.split(';')
    are_all_sets_valid = True
    max_red = 0
    max_green = 0
    max_blue = 0
    for set in sets:
        rounds = set.split(',')
        set_dict = {}
        for round in rounds:
            num, color = round.strip().split(' ')
            set_dict[color] = int(num)
        red = set_dict.get('red', 0)
        green = set_dict.get('green', 0)
        blue = set_dict.get('blue', 0)
        max_red = red if red > max_red else max_red
        max_blue = blue if blue > max_blue else max_blue
        max_green = green if green > max_green else max_green
        if red > limits['red'] or blue > limits['blue'] or green > limits['green']:
            are_all_sets_valid = False
    powers.append(max_red * max_green * max_blue)
    if are_all_sets_valid:
        valid_games.append(id)

print(sum(valid_games))
print(sum(powers))

