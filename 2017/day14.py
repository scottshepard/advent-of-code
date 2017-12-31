
# key is vbqugkhl
# 
# python -m day14 vbqugkhl

import sys
import os

from day10 import KnotHash

def solve(input):
	total = 0
	for i in list(range(128)):
		key = input + '-' + str(i)
		row = knot_hash_row(key)
		total += row_sum(row)
	return total

def row_sum(row):
	total = 0
	return sum([int(c) for c in list(row)])

def knot_hash_row(row):
	hashed = list(KnotHash(row).hash)
	return ''.join([binchar(h) for h in hashed])

def binchar(char):
	return format(int(char, 16), '0>4b')

if __name__ == '__main__':
	print(solve(sys.argv[1]))