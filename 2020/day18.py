from utils import read_input


def evaluate(exp, mode=1):
    while '(' in exp:
        right_par_count = 0
        i = 0
        while right_par_count == 0:
            if exp[i] == '(':
                left_par_i = i
            elif exp[i] == ')':
                right_par_count += 1
                right_par_i = i
            i += 1
        num = evaluate(exp[left_par_i+1:right_par_i], mode)
        exp = exp[:left_par_i] + str(num) + exp[right_par_i+1:]
    if mode == 2:
        while '+' in exp:
            exp = exp.split(' ')
            i = exp.index('+')
            num = eval(''.join(exp[i-1:i+2]))
            exp = ' '.join(exp[:i-1]) + ' ' + str(num) + ' ' + ' '.join(exp[i+2:])
            exp = exp.strip()
    exp = exp.split(' ')
    if len(exp) == 1:
        return int(exp[0])
    k1 = exp[0]
    k2 = exp[2]
    op = exp[1]
    tot = eval(k1 + op + k2)
    if len(exp) == 3:
        return tot
    else:
        exp = exp[3:]
        exp.insert(0, str(tot))
        exp = ' '.join(exp)
        return evaluate(exp, mode)

assert evaluate('1 + 2 * 3 + 4 * 5 + 6') == 71
assert evaluate('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert evaluate('2 * 3 + (4 * 5)') == 26
assert evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
assert evaluate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
assert evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

assert evaluate('1 + 2 * 3 + 4 * 5 + 6', 2) == 231
assert evaluate('1 + (2 * 3) + (4 * (5 + 6))', 2) == 51
assert evaluate('2 * 3 + (4 * 5)', 2) == 46
assert evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)', 2) == 1445
assert evaluate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 2) == 669060
assert evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 2) == 23340


def solve(input, mode):
    return sum([evaluate(line, mode) for line in input])


real_input = read_input('day18.txt')
print('Part 1:', solve(real_input, mode=1))
print('Part 2:', solve(real_input, mode=2))
