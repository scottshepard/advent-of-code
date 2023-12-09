from utils import read_input
import regex as re

input = read_input('day01.txt')

part1 = 0
for line in input:
    digits = re.findall('[0-9]', line)
    part1 += int(digits[0] + digits[-1])

print(part1)

digits_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
    # 'zero': '0'
}

part2 = 0
for line in input:
    digits = re.findall('|'.join(list(digits_map.keys()))+'|[0-9]', line, overlapped=True) # overlapped bc oneight needs to resolve to 18
    digits = [digits_map[d] if d in digits_map else d for d in digits]
    part2 += int(digits[0] + digits[-1])

print(part2)