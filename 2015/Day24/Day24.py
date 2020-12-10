import os
import numpy as np
import pdb


def read_input(file, split_char='\n'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    f = open(file_path)
    data = f.read().split(split_char)
    if data[-1] == '':
        data.pop(-1)
    return [int(d) for d in data]

def sorted_k_partitions(seq, k):
    """Returns a list of all unique k-partitions of `seq`.

    Each partition is a list of parts, and each part is a tuple.

    The parts in each individual partition will be sorted in shortlex
    order (i.e., by length first, then lexicographically).

    The overall list of partitions will then be sorted by the length
    of their first part, the length of their second part, ...,
    the length of their last part, and then lexicographically.
    """
    n = len(seq)
    groups = []  # a list of lists, currently empty

    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    pdb.set_trace()
                    yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)

    # Sort the parts in each partition in shortlex order
    result = [sorted(ps, key = lambda p: (len(p), p)) for ps in result]
    # Sort partitions by the length of each part, then lexicographically.
    result = sorted(result, key = lambda ps: (*map(len, ps), ps))

    return result

def find_balanced_groups(groups):
    even_groups = []
    for g in groups:
        if all([sum(k)==sum(g[0]) for k in g]):
            even_groups.append(g)
    return even_groups

def smallest_first_group(groups):
    narrowed = []
    size1 = len(groups)
    for eg in groups:
        if len(eg[0]) <= size1:
            size1 = len(eg[0])
            narrowed.append(eg[0])
    return list(set(narrowed))

def smallest_quantum_entaglement(groups):
    results = []
    for g in groups:
        [np.product(k) for k in g]

sample_input = [1,2,3,4,5,7,8,9,10,11]
real_input = read_input('day24.txt')

groups = sorted_k_partitions(sample_input, 3)
print(len(groups))
even_groups = find_balanced_groups(groups)
print(len(even_groups))
smallest_1st_groups = smallest_first_group(even_groups)
print(len(smallest_first_group()))

