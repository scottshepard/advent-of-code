from utils import read_input
import re

input = read_input('day02.txt')

def is_valid(args_tupl, part=1):
    pwd = args_tupl[0]
    low = args_tupl[1]
    high = args_tupl[2]
    letter = args_tupl[3]
    if part == 1:
        instances = pwd.count(letter)
        return low <= instances <= high
    else:
        return (pwd[low-1] == letter) != (pwd[high-1] == letter)

assert is_valid(('abcde', 1, 3, 'a'))
assert not is_valid(('cdefg', 1, 3, 'b'))

def extract(pattern, string):
    try:
        found = re.search(pattern, string).group(1)
    except:
        found = ''
    return found

def parse_line(line):
    low = int(extract('(^[0-9]+)', line))
    high = int(extract('(?<=-)([0-9]+)', line))
    letter = extract(' ([a-zA-Z]){1}', line)
    pwd = extract('([^ ]+)$', line)
    return pwd, low, high, letter

assert is_valid(parse_line('1-3 a: abcde'), 2)
assert not is_valid(parse_line('1-3 b: cdefg'), 2)
assert not is_valid(parse_line('2-9 c: ccccccccc'), 2)


n_valid_1 = 0
n_valid_2 = 0
for line in input:
    n_valid_1 += int(is_valid(parse_line(line), 1))
    n_valid_2 += int(is_valid(parse_line(line), 2))

print('Part 1: ', n_valid_1)
print('Part 2: ', n_valid_2)

