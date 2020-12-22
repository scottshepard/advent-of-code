from utils import read_input


def evaluate(exp):
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
        num = evaluate(exp[left_par_i+1:right_par_i])
        exp = exp[:left_par_i] + str(num) + exp[right_par_i+1:]
    exp = exp.split(' ')
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
        return evaluate(exp)

assert evaluate('1 + 2 * 3 + 4 * 5 + 6') == 71
assert evaluate('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert evaluate('2 * 3 + (4 * 5)') == 26
assert evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
assert evaluate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
assert evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

real_input = read_input('day18.txt')

sum = 0
for line in real_input:
    sum += evaluate(line)
print('Part 1:', sum)

