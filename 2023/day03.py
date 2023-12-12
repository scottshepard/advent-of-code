from utils import read_input
import pdb
import string
import re

input = read_input('day03.txt')


def _is_character(y, x):
    special_characters = string.punctuation.replace('.', '')
    try:
        char = input[y][x]
        return char in special_characters
    except:
        return False


j = 0
valids = []
gears = []
while j < len(input):
    i = 0
    while i < len(input[0]):
        c = input[j][i]
        k = 0
        if c.isnumeric():
            while c.isnumeric():
                k += 1
                if k + i >= len(input[0]):
                    break
                c = input[j][i+k]
            is_valid = False
            for l in range(k):
                is_valid = \
                    is_valid or \
                    _is_character(j-1, i+l) or \
                    _is_character(j-1, i+l-1) or \
                    _is_character(j-1, i+l+1) or \
                    _is_character(j+1, i+l-1) or \
                    _is_character(j+1, i+l) or \
                    _is_character(j+1, i+l+1) or \
                    _is_character(j, i+l+1) or \
                    _is_character(j, i+l-1)
            if is_valid:
                num = input[j][i:i+k]
                valids.append(int(num))

        i += 1+k
    j += 1

j = 0
gears = []
while j < len(input):
    i = 0
    while i < len(input[0]):
        c = input[j][i]
        if c == '*':
            nums = []
            for jj in range(-1, 2):
                if j + jj < 0 or j + jj >= len(input):
                    continue
                ii = -1
                while ii <= 1:
                    if i + ii < 0 or i + ii >= len(input[0]):
                        continue
                    c = input[j + jj][i + ii]
                    ii_minus = 0
                    while (i + ii + ii_minus >= 0) and input[j + jj][i + ii + ii_minus].isnumeric():
                        ii_minus -= 1
                    ii_plus = 0
                    while (i + ii + ii_plus < len(input[0])) and input[j + jj][i + ii + ii_plus].isnumeric():
                        ii_plus += 1
                    if ii_minus < 0 or ii_plus > 0:
                        nums.append(int(input[j + jj][i + ii + ii_minus + 1:i + ii + ii_plus]))
                    ii += max(ii_plus, 1)
            if len(nums) == 2:
                gears.append(nums)
        i += 1
    j += 1

print(sum(valids))
print(sum(map(lambda g: g[0] * g[1], gears)))

# wrong: 73288721
# wrong: 74003916
# right: 84159075
