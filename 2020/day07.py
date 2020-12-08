import re
from utils import read_input
import pdb





def extract_colors(rule):
    m = re.search('([a-z]+\s[a-z]+)', rule)
    try:
        r = m.group(1)
    except:
        r = ''
    if r == 'no other':
        r = ''
    m = re.search('([0-9]+)', rule)
    try:
        n = int(m.group(1))
    except:
        n = ''
    return (r, n)

def create_tree(rules):
    tree = {}
    for rule in rules:
        parts = rule.split(r' contain ')
        key = re.search('([a-z]+\s[a-z]+)', parts[0]).group(1)
        values = [extract_colors(p) for p in parts[1].split(', ')]
        if values == [('', '')]:
            values = ''
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
            for bag in tree[k]:
                if n in bag:
                    new_nodes.append(k)
    return new_nodes

test_input = read_input('day07_test.txt')
test_tree = create_tree(test_input)

assert _count_parents(test_tree, ['shiny gold']) == ['bright white', 'muted yellow']
assert count_parents(test_tree, 'shiny gold') == 4

input = read_input('day07.txt')
tree = create_tree(input)
print('Part 1:', count_parents(tree, 'shiny gold'))

def count_children(tree, node):
    if tree[node] == '':
        return 0
    else:
        count = 0
        for bag in tree[node]:
            count += (count_children(tree, bag[0]) + 1) * bag[1]
        return count

assert count_children(test_tree, 'shiny gold') == 32
print('Part 2:', count_children(tree, 'shiny gold'))






