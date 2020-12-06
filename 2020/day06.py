import re
from utils import read_input


def questions_answered_yes(group):
    group = re.sub('\n', '', group)
    matches = re.findall(r'[a-z]', group)
    return len(set(matches))

def all_answered_yes(group):
    data = group.split('\n')
    if data[-1] == '':
        data.pop(-1)
    n_people = len(data)
    matches = list(set(re.findall(r'[a-z]', group)))
    result = 0
    for m in matches:
        if len(re.findall(m, group)) == n_people:
            result += 1
    return result

sample_input = read_input('day06_test.txt', '\n\n')
assert sum([questions_answered_yes(g) for g in sample_input]) == 11
assert sum([all_answered_yes(g) for g in sample_input]) == 6

input = read_input('day06.txt', '\n\n')
print('Part 1:', sum([questions_answered_yes(g) for g in input]))
print('Part 2:', sum([all_answered_yes(g) for g in input]))
