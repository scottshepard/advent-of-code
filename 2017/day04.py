# --- Day 4: High-Entropy Passphrases ---
#
# A new system policy has been put in place that requires all accounts to use a 
# passphrase instead of simply a password. A passphrase consists of a series of 
# words (lowercase letters) separated by spaces.
#
# To ensure security, a valid passphrase must contain no duplicate words.
#
# For example:
#
# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.
# The system's full passphrase list is available as your puzzle input. 
# How many passphrases are valid?
# Answer: 337
# 
# --- Part Two ---
#
# For added security, yet another system policy has been put in place. 
# Now, a valid passphrase must contain no two words that are anagrams of each 
# other - that is, a passphrase is invalid if any word's letters can be 
# rearranged to form any other word in the passphrase.
#
# For example:
#
# abcde fghij is a valid passphrase.
# abcde xyz ecdab is not valid - the letters from the third word can be 
# rearranged to form the first word.
# a ab abc abd abf abj is a valid passphrase, because all letters need to be 
# used when forming another word.
# iiii oiii ooii oooi oooo is valid.
# oiii ioii iioi iiio is not valid - any of these words can be rearranged to 
# form any other word.
# Under this new system policy, how many passphrases are valid?
# Answer: 231
# ------------------------------------------------------------------------------

import itertools
import re
from sys import argv
import os

def solve1(phrases):
    return sum([valid_passphrase1(phrase) for phrase in phrases])

def valid_passphrase1(phrase):
    words = phrase.split()
    return len(words) == len(set(words))

def solve2(phrases):
    return sum([valid_passphrase2(phrase) for phrase in phrases])

def valid_passphrase2(phrase):
    return (not has_anagram(phrase)) & valid_passphrase1(phrase)

def has_anagram(phrase):
    words = phrase.split()
    combos = itertools.combinations(words, 2)
    return any([is_anagram(c[0], c[1]) for c in combos])

def is_anagram(w1, w2):
    return sorted(list(w1)) == sorted(list(w2))

if __name__ == '__main__':
    if (len(argv) == 2):
        data = argv[1]
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs/day04.txt")
        f = open(file_path)
        data = f.read()
    passphrases = data.split('\n')
    print(solve1(passphrases))
    print(solve2(passphrases))
    
