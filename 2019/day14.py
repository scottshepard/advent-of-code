from utils import read_input
import pdb


def parse_lines(lines):
    reactions = {}
    for line in lines:
        out, reactions = parse_line(line)
        reactions[out] = reactions
    return reactions

def parse_line(line):
    left, right = line.split('=>')
    ingredients = []
    left = left.strip().split(',')
    for l in left:
        l = l.strip().split(' ')
        out = l[1]
        quant = int(l[0])
        ingredients.append((out, quant))
    right = right.strip().split(' ')
    out = right[-1]
    quant = int(right[-2])
    return out, {'quant': quant, 'ingredients': ingredients}


assert parse_line('7 A, 1 B => 1 C') == ('C', {'quant': 1, 'ingredients': [('A', 7), ('B', 1)]})

test_input1 = read_input('day14_test1.txt')



