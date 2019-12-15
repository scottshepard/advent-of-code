
def is_valid_password(pwd, part2=False):
    adjacent_digits = False
    never_decreasing = True
    pwd = [int(i) for i in str(pwd)]
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1]:
            if part2:
                if (i == 0 or pwd[i-1] != pwd[i]) and (i == len(pwd)-2 or pwd[i+2] != pwd[i]):
                    adjacent_digits = True
            else:
                adjacent_digits = True
        if pwd[i] > pwd[i+1]:
            never_decreasing = False
    return adjacent_digits and never_decreasing

def is_within_range(pwd, r1, r2):
    return (pwd >= r1 and pwd <= r2)

def solve(r1, r2, part2=False):
    total = 0
    for num in range(r1, r2):
        if is_valid_password(num, part2):
            total += 1
    return total


if __name__ == '__main__':
    pwd_range = [245182, 790572]
    assert(is_valid_password(111111))
    assert(not is_valid_password(223450))
    assert (not is_valid_password(123789))
    print('Solution for part 1 is {}'.format(solve(245182, 790572)))

    assert(is_valid_password(112233, True))
    assert(not is_valid_password(123444, True))
    assert(is_valid_password(111122, True))
    print('Solution for part 2 is {}'.format(solve(245182, 790572, True)))
