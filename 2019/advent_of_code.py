import os

def read_input(file):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs/{0}".format(file))
    f = open(file_path)
    data = f.read().split('\n')
    if data[-1] == '':
        data.pop(-1)
    return data


