import re


def decompress(text):
    '''Only decompresses string up to the first compression after n index'''
    text = re.sub('\s', '', text)
    search = re.search('\([0-9]+x[0-9]+\)', text)
    if search is None:
        return text
    start = search.start()
    end = search.end()
    match = search.group(0)
    pre_match = text[:start]
    char_len = int(re.search('[0-9]+(?=x)', match).group(0))
    repeats = int(re.search('(?<=x)[0-9]+', match).group(0))
    matched_chars = text[end:(end+char_len)]
    decompressed_section = matched_chars * repeats
    remaining = text[(end+char_len):]
    return pre_match + decompress(decompressed_section) + decompress(remaining)

if __name__ == '__main__':
    fileobject = open('inputs/day09.txt')
    data = fileobject.read()
    lines = re.split('\n', data)
    print(sum([len(decompress(line)) for line in lines]))
