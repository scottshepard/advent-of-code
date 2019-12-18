from utils import read_input
import pdb


def parse_lines(lines):
    all_reactions = {}
    for line in lines:
        out, reactions = parse_line(line)
        all_reactions[out] = reactions
    return all_reactions

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

def how_much(chem, need, reactions):
    reactions_ = reactions[chem]
    quant = reactions_['quant']


assert parse_line('7 A, 1 B => 1 C') == ('C', {'quant': 1, 'ingredients': [('A', 7), ('B', 1)]})

test_input1 = read_input('day14_test1.txt')

reactions = parse_lines(test_input1)

