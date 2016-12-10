# --- Day 9: Explosives in Cyberspace ---
#
# Wandering around a secure area, you come across a datalink port to a new part
# of the network. After briefly scanning it for interesting files, you find one
# file in particular that catches your attention. It's compressed with an 
# experimental format, but fortunately, the documentation for the format is 
# nearby.
#
# The format compresses a sequence of characters. Whitespace is ignored. To 
# indicate that some sequence should be repeated, a marker is added to the 
# file, like (10x2). To decompress this marker, take the subsequent 10 
# characters and repeat them 2 times. Then, continue reading the file after the
# repeated data. The marker itself is not included in the decompressed output.
#
# If parentheses or other characters appear within the data referenced by a 
# marker, that's okay - treat it like normal data, not a marker, and then 
# resume looking for markers after the decompressed section.
#
# For example:
#
# ADVENT contains no markers and decompresses to itself with no changes, 
# resulting in a decompressed length of 6.
# A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a 
# decompressed length of 7.
# (3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
# A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a 
# decompressed length of 11.
# (6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but 
# because it's within a data section of another marker, it is not treated any 
# differently from the A that comes after it. It has a decompressed length of 6
# X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18) 
# because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped
# and not processed further.
# What is the decompressed length of the file (your puzzle input)? 
# Don't count whitespace.
#
# -----------------------------------------------------------------------------

import re

def decompress(text):
    # Remove whitespace
    text = re.sub('\s', '', text)
    # Find the first decompress code match
    # i.e. (1x10)
    search = re.search('\([0-9]+x[0-9]+\)', text)
    # Base case, if no match found then output the original text
    if search is None:
        return text
    # Record indicies for start and end of the match
    start = search.start()
    end = search.end()
    # Any text before the match needs to be returned with the final output
    pre_match = text[:start]
    # Get the match text
    match = search.group(0)
    # Find the number of characters to coutn and how many repititions
    char_len = int(re.search('[0-9]+(?=x)', match).group(0))
    repeats = int(re.search('(?<=x)[0-9]+', match).group(0))
    # Get the text to repeat and calculate the decompressed section
    matched_chars = text[end:(end+char_len)]
    decompressed_section = matched_chars * repeats
    # The text at the end might contain another decompression code, 
    # so return the current decompressed_section and decompress
    # that section too
    remaining = text[(end+char_len):]
    return pre_match + decompressed_section + decompress(remaining)

def calculate_decompress_len(text):
    search = re.search('\([0-9]+x[0-9]+\)', text)
    if search is None:
        return len(text)
    start = search.start()
    end = search.end()
    pre_match_len = len(text[:start])
    match = search.group(0)
    char_len = int(re.search('[0-9]+(?=x)', match).group(0))
    repeats = int(re.search('(?<=x)[0-9]+', match).group(0))
    matched_chars = text[end:(end+char_len)]
    search_matched = re.search('\([0-9]+x[0-9]+\)', matched_chars)
    if search_matched is None:
        matched_len = char_len * repeats
    else:
        matched_len = calculate_decompress_len(matched_chars) * repeats
    remaining = text[(end+char_len):]
    return pre_match_len + matched_len + calculate_decompress_len(remaining)

if __name__ == '__main__':
    fileobject = open('inputs/day09.txt')
    data = fileobject.read()
    lines = re.split('\n', data)
    print('Part 1:', sum([len(decompress(line)) for line in lines]))
    # Correct answer is 110346
    print('Part 2:', sum([calculate_decompress_len(line) for line in lines]))
    # Correct answer is 10774309173
