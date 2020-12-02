from utils import read_input


input = read_input('day01.txt')


def sum_to(num, lst, n=2):
    '''
    :param num: Number to sum to
    :param lst: List of ints
    :return: Two elements in the lst that sum to the num
    '''
    lst = [int(x) for x in lst]
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if n == 2:
                if lst[i] + lst[j] == num:
                    return lst[i], lst[j]
            if n == 3:
                for k in range(j, len(lst)):
                    if lst[i] + lst[j] + lst[k] == num:
                        return lst[i], lst[j], lst[k]

x, y = sum_to(2020, input)
print('Part 1:', x * y)

x, y, z = sum_to(2020, input, 3)
print('Part 2:', x * y * z)
