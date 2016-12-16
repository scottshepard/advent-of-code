def generate_data(input_):
    a = input_
    b = ''.join(['1' if x == '0' else '0' for x in list(input_[::-1])])
    return a + '0' + b

def generate_enough_data(input_, target_len):
    while len(input_) < target_len:
        input_ = generate_data(input_)
    return input_[:target_len]

def string_split(input_, n=2):
    return [input_[i:i+n] for i in range(0, len(input_), n)]

def same_different(input_):
    pairs = string_split(input_)
    output = []
    for pair in pairs:
        if pair[0] == pair[1]:
            output.append('1')
        else:
            output.append('0')
    return ''.join(output)

def checksum(input_):
    cs = same_different(input_)
    if len(cs) % 2 == 0:
        return checksum(cs)
    else:
        return cs

if __name__ == '__main__':
    input_ = '10001110011110000'
    length1 = 272
    print('Part 1:', checksum(generate_enough_data(input_, length1)))
    length2 = 35651584
    print('Part 2:', checksum(generate_enough_data(input_, length2)))
