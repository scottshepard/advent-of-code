# --- Day 14: One-Time Pad ---
#
# In order to communicate securely with Santa while you're on this mission, you've been using a one-time pad that you generate using a pre-agreed algorithm. Unfortunately, you've run out of keys in your one-time pad, and so you need to generate some more.
#
# To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt (your puzzle input) and an increasing integer index (starting with 0) as a string of lowercase hexadecimal digits.
#
# However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. A hash is a key only if:
#
# It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
# One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.
# Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, regardless of whether the current hash is a key, always resume testing for keys starting with the very next hash.
#
# For example, if the pre-arranged salt is abc:
#
# The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes (index 19 through index 1018) contain 88888.
# The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: one of the next thousand hashes (the one at index 816) contains eeeee.
# None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200 contains 99999.
# Eventually, index 22728 meets all of the criteria to generate the 64th key.
# So, using our example salt of abc, index 22728 produces the 64th key.
#
# Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?
#
# Your puzzle input is yjdafjpo.
#
# ----------------------------------------------------------------------------

from hashlib import md5
import re
import sys
sys.setrecursionlimit(3000)

digests = {}

def getMD5(salt, i, n=0):
    key = salt + '_' + str(i) + '_' + str(n)
    if key in digests:
        return digests[key] 
    else:
        digests[key] = encode(salt + str(i), n)
        return digests[key]

def encode(string, n=0):
    hashed = md5(string.encode('utf-8')).hexdigest() 
    if n == 0:
       return hashed 
    else:
        return encode(hashed, n-1)

def interesting1(string, n=3):
    search = re.search('(.)\\1{{{0},}}'.format(n-1), string) 
    if search is None:
        return False
    else:
        return search.group(0)

def interesting2(string, char, n=5):
    search = re.search(r'({0})\1{{{1},}}'.format(char, n-1), string) 
    if search is None:
        return False
    else:
        return search.group(0)

def five_repeats_in_next_1000_hashes(salt, char, index, hash_times=0):
    for j in range(index+1, index+1001):
        hashed = getMD5(salt, j, hash_times)
        second_match_found = interesting2(hashed, char)
        if second_match_found:
           return True
    return False

def solve_day14(salt, n_keys=64, hash_times = 0):
    keys = []
    i = 0
    while len(keys) < n_keys:
        hashed = getMD5(salt, i, hash_times)
        first_match = interesting1(hashed)
        if first_match:
            char = first_match[0]
            if five_repeats_in_next_1000_hashes(salt, char, i, hash_times):
                keys.append(i)
        i += 1
    return keys

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("This script needs an input string as a", 
              "command-line argument to work")
    else:
        keys = solve_day14(sys.argv[1])
        print('Part 1:', keys[len(keys)-1])
        keys2 = solve_day14(sys.argv[1], hash_times=2016)
        print('Part 2:', keys2[len(keys2)-1])

