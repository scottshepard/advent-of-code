# --- Day 7: Internet Protocol Version 7 ---
#
# While snooping around the local network of EBHQ, you compile a list of IP 
# addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to 
# figure out which IPs support TLS (transport-layer snooping).
#
# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
# An ABBA is any four-character sequence which consists of a pair of two 
# different characters followed by the reverse of that pair, such as xyyx or 
# abba. However, the IP also must not have an ABBA within any hypernet 
# sequences, which are contained by square brackets.
#
# For example:
#
# abba[mnop]qrst supports TLS (abba outside square brackets).
# abcd[bddb]xyyx does not support TLS (bddb is within square brackets, 
# even though xyyx is outside square brackets).
# aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters
# must be different).
# ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even 
# though it's within a larger string).
# How many IPs in your puzzle input support TLS?
#
# --- Part Two ---
#
# You would also like to know which IPs support SSL (super-secret listening).
#
# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in 
# the supernet sequences (outside any square bracketed sections), and a 
# corresponding Byte Allocation Block, or BAB, anywhere in the hypernet 
# sequences. An ABA is any three-character sequence which consists of the same 
# character twice with a different character between them, such as xyx or aba. 
# A corresponding BAB is the same characters but in reversed positions: yxy and
# bab, respectively.
#
# For example:
#
# aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab 
# within square brackets).
# xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
# aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet;
# the aaa sequence is not related, because the interior character must be 
# different).
# zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a 
# corresponding bzb, even though zaz and zbz overlap).
# How many IPs in your puzzle input support SSL?
#
# -----------------------------------------------------------------------------

import re

def supports_tls(string):
    '''Determines is a string supports TLS. It must
       1. Have an ABBA pair in a nonhypertext string
       2. Must not have an ABBA pair in a hypertext string'''
    nonhypernet = nonhypernet_text(string)
    hypernet = hypernet_text(string)
    a = detect_abba_in_list(nonhypernet)
    b = detect_abba_in_list(hypernet)
    return (a and not b)

def supports_ssl(string):
    '''Determines if a string supports ssl. It must:
       1. Have an ABA pair in a nonhypertext string
       2. Have a corresponding BAB pari in a hypertext string'''
    nhtxt = nonhypernet_text(string)
    htxt = hypernet_text(string)
    abas = find_abas_in_list(nhtxt)
    return any([detect_bab_in_list(htxt, aba) for aba in abas])

def nonhypernet_text(string):
    '''Returns a list of all nonhypertext, all text not found between
       square brackets'''
    if re.search('\[', string) is None:
        return string
    between_htxt = re.findall(r"\]([A-Za-z0-9_]+)\[", string)
    before_htxt = re.findall(r"([A-Za-z0-9_]+)\[", string)
    after_htxt = re.findall(r"]([A-Za-z0-9_]+)", string)
    return between_htxt + before_htxt + after_htxt

def hypernet_text(string):
    '''Return a list of all text found between square brackets
       i.e. [xxyy]asdjfkl[aabbaa] => ['xxyy', 'aabbaa']'''
    return re.findall(r"\[([A-Za-z0-9_]+)\]", string)

def detect_abba_in_list(list_strings):
    bools = []
    for string in list_strings:
        for seq in all_nletter_seqs(string, 4):
            bools.append(abba(seq))
    return any(bools)

def find_abas_in_list(list_strings):
    abas = []
    for string in list_strings:
        for seq in all_nletter_seqs(string, 3):
            if aba(seq):
                abas.append(seq)
    return abas

def detect_bab_in_list(list_strings, aba):
    bools = []
    for string in list_strings:
        for seq in all_nletter_seqs(string, 3):
            bools.append(bab(seq, aba))
    return any(bools)

def abba(string):
    if(len(string) < 4):
        return False
    elif(string[0] == string[1]):
        return False
    else:
        return string[0:2] == ''.join(list(reversed(string[2:4])))

def aba(string):
    if(len(string) < 3):
        return False
    elif(string[0] == string[1]):
        return False
    else:
        return string[0] == string[2]

def bab(string, aba):
    return string == (aba[1] + aba[0] + aba[1])

def all_nletter_seqs(string, n):
    if len(string) < n:
        return []
    else:
        chars = list(string)
        sets = []
        for i in range(0, len(chars)-(n-1)):
            sets.append(''.join(chars[i:i+n]))
        return sets

if __name__ == '__main__':
    fileobject = open('inputs/day07.txt')
    data = fileobject.read()
    lines = re.split('\n', data)
    print("Part 1:", sum([supports_tls(line) for line in lines]))
    print("Part 1:", sum([supports_ssl(line) for line in lines]))
