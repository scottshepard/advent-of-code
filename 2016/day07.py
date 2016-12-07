import re

def supports_tls(string):
    nhtxt = nonhypernet_text(string)
    htxt = hypernet_text(string)
    a = detect_abba_in_list(nhtxt)
    b = detect_abba_in_list(htxt)
    return (a and not b)

def supports_ssl(string):
    nhtxt = nonhypernet_text(string)
    htxt = hypernet_text(string)
    abas = find_abas_in_list(nhtxt)
    return any([detect_bab_in_list(htxt, aba) for aba in abas])

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

def hypernet_text(string):
    return re.findall(r"\[([A-Za-z0-9_]+)\]", string)

def all_nletter_seqs(string, n):
    if len(string) < n:
        return []
    else:
        chars = list(string)
        sets = []
        for i in range(0, len(chars)-(n-1)):
            sets.append(''.join(chars[i:i+n]))
        return sets

def nonhypernet_text(string):
    if re.search('\[', string) is None:
        return string
    between_htxt = re.findall(r"\]([A-Za-z0-9_]+)\[", string)
    before_htxt = re.findall(r"([A-Za-z0-9_]+)\[", string)
    after_htxt = re.findall(r"]([A-Za-z0-9_]+)", string)
    return between_htxt + before_htxt + after_htxt

if __name__ == '__main__':
    fileobject = open('inputs/day07.txt')
    data = fileobject.read()
    lines = re.split('\n', data)
    print("Part 1:", sum([supports_tls(line) for line in lines]))
    print("Part 1:", sum([supports_ssl(line) for line in lines]))
    



