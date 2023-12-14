from utils import read_input
from itertools import pairwise
import pdb

input = read_input('day05.txt', '\n\n')
input[-1] = input[-1][:-1]
seeds = list(map(int, input[0].split(' ')[1:]))


maps = []
for map in input[1:]:
    lines = map.split('\n')
    _from, _, _to = lines[0].replace(' map:', '').split('-')
    maps.append({'from': _from, 'to': _to, 'rules': [[int(x) for x in l.split(' ')] for l in lines[1:]]})


def find_location_number(seed):
    results = {
        'seed': seed
    }
    for map in maps:
        # print(map)
        type = map['to']
        for line in map['rules']:
            # pdb.set_trace()
            if line[1] <= seed < line[1]+line[2]:
                results[type] = seed-line[1]+line[0]
        results[type] = results.get(type, seed)
        seed = results[type]
    return results['location']


print(min([find_location_number(seed) for seed in seeds]))
