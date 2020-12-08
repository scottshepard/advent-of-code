import re
from utils import read_input
import pdb





def extract_color(rule):
    m = re.search('([a-z]+\s[a-z]+)', rule)
    try:
        r = m.group(1)
    except:
        r = ''
    if r == 'no other':
        r = ''
    return r

def create_tree(rules):
    tree = {}
    for rule in rules:
        parts = rule.split(r' contain ')
        key = extract_color(parts[0])
        values = [extract_color(p) for p in parts[1].split(', ')]
        tree[key] = values
    return tree



def count_parents(tree, node):
    parents = []
    x = _count_parents(tree, [node])
    while x != []:
        x = list(set(x))
        parents.extend(x)
        parents = list(set(parents))
        x = _count_parents(tree, x)
    return len(list(set(parents)))

def _count_parents(tree, nodes):
    new_nodes=[]
    for k in tree:
        #pdb.set_trace()
        for n in nodes:
            if n in tree[k]:
                new_nodes.append(k)
    return new_nodes

test_input = read_input('day07_test.txt')
test_tree = create_tree(test_input)

assert _count_parents(test_tree, ['shiny gold']) == ['bright white', 'muted yellow']
assert count_parents(test_tree, 'shiny gold') == 4

input = read_input('day07.txt')
tree = create_tree(input)
print('Part 1:', count_parents(tree, 'shiny gold'))





