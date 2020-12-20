from utils import read_input


def parse_input(input):
    i = 0
    line = input[i]
    ranges = {}
    while line != '':
        type, r1, _, r2 = line.split(' ')
        type = type.replace(':', '')
        r0, r1 = r1.split('-')
        r2, r3 = r2.split('-')
        ranges[type] = [range(int(r0), int(r1)+1), range(int(r2), int(r3)+1)]
        i += 1
        line = input[i]
    i += 2
    line = input[i]
    your_ticket = [int(l) for l in line.split(',')]
    i += 3
    line = input[i]
    other_tickets = []
    while line != '':
        other_tickets.append([int(l) for l in line.split(',')])
        i += 1
        line = input[i]
    return ranges, your_ticket, other_tickets


def solve_part_1(ranges, tickets):
    invalid_nums = []
    valid_tix = []
    for tix in tickets:
        valid = True
        for n in tix:
            if not valid_num(n, ranges):
                valid = False
                invalid_nums.append(n)
        if valid:
            valid_tix.append(tix)
    return sum(invalid_nums), valid_tix

def valid_num(n, ranges):
    valid = False
    for r in ranges.values():
        if (n in r[0]) or (n in r[1]):
            valid = True
    return valid

test_input = read_input('day16_test.txt')
ranges, yt, ot = parse_input(test_input)

assert valid_num(7, ranges)
assert not valid_num(4, ranges)
invalid_sum, valid_tix = solve_part_1(ranges, ot)
assert invalid_sum == 71

test_input2 = read_input('day16_test2.txt')
ranges, yt, ot = parse_input(test_input2)
invalid_sum, valid_tix = solve_part_1(ranges, ot)

def determine_correct_ticket_positions(ranges, valid_tix):
    # First part builds up all valid positions for each ticket section type
    #
    # Example:
    # class: 0 - 1 or 4 - 19
    # row: 0 - 5 or 8 - 19
    # seat: 0 - 13 or 16 - 19
    #
    # nearby tickets:
    # 3,9,18
    # 15,1,5
    # 5,14,9
    #
    # Output: {'class': [1, 2], 'row': [0, 1, 2], 'seat': [2]}
    valid_pos = {}
    for r in ranges:
        for i in range(len(valid_tix[0])):
            pos_in_range = []
            for j in range(len(valid_tix)):
                pos_in_range.append((valid_tix[j][i] in ranges[r][0]) or (valid_tix[j][i] in ranges[r][1]))
            if all(pos_in_range):
                if r in valid_pos:
                    valid_pos[r].append(i)
                else:
                    valid_pos[r] = [i]
    # Now that all valid positions for each type have been identified, it needs to be narrowed down.]
    # This next part iterates through and narrows down the set
    # Example:
    # {'class': [1, 2], 'row': [0, 1, 2], 'seat': [2]} => {'class': 1, 'row': 0, 'seat': 2}
    correct_pos = {}
    while len(correct_pos) < len(valid_pos):
        for vp in valid_pos:
            if len(valid_pos[vp]) == 1:
                elm = valid_pos[vp][0]
                correct_pos[vp] = elm
                for vp2 in valid_pos:
                    try:
                        valid_pos[vp2].remove(elm)
                    except:
                        pass
    return correct_pos


positions = determine_correct_ticket_positions(ranges, valid_tix)
assert positions == {'seat': 2, 'class': 1, 'row': 0}

real_input = read_input('day16.txt')
ranges, tix, ot = parse_input(real_input)
invalid_sum, valid_tix = solve_part_1(ranges, ot)
print('Part 1:', invalid_sum)

positions = determine_correct_ticket_positions(ranges, valid_tix)

result = 1
for pos in positions:
    if 'departure' in pos:
        result *= tix[positions[pos]]
print('Part 2:', result)


