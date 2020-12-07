import re
from utils import read_input



test_input = read_input('day07_test.txt')


def extract_color(rule):
    m = re.search('([a-z]+\s[a-z]+)', rule)
    try:
        r = m.group(1)
    except:
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

