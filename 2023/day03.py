from utils import read_input
import pdb
import string

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
while j < len(input):
    # print(j)
    i = 0
    while i < len(input[0]):
        c = input[j][i]
        # print(c)
        k = 0
        if c.isnumeric():
            while c.isnumeric():
                k += 1
                if k + i >= len(input[0]):
                    break
                c = input[j][i+k]
            is_valid = False
            for l in range(k):
                # if c == '3':
                # pdb.set_trace()
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

print(sum(valids))
