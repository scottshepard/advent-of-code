import os
import np
import pdb


def read_input(file, split_char='\n'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    f = open(file_path)
    data = f.read().split(split_char)
    if data[-1] == '':
        data.pop(-1)
    return [int(d) for d in data]

sample_input = [1,2,3,4,5,7,8,9,10,11]
real_input = read_input('day24.txt')



