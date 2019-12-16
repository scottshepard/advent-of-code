import math
import numpy as np
from utils import read_input
import pdb

def generate_pattern_matrix(base, n_signal):
    base_mat = np.ones((1, n_signal))
    for j in range(1, n_signal+1):
        repeated_base = [i for i in base for _ in range(j)]
        repeated_base = repeated_base * (math.ceil(n_signal / len(base)) + 1)
        repeated_base.pop(0)
        repeated_base = repeated_base[:n_signal]
        # pdb.set_trace()
        base_mat = np.append(base_mat, [repeated_base], axis=0)
    base_mat = np.delete(base_mat, 0, 0)
    return base_mat

def fft_once(signal, pattern_matrix):
    signal = [int(i) for i in list(signal)]
    signal_mat = np.array([signal,]*int(len(signal)/2))
    mat = signal_mat * pattern_matrix
    front_half = ''.join([str(int(sum(row)))[-1] for row in mat])
    back_half = backwards_cumsum(signal[int(len(signal) / 2):])
    # pdb.set_trace()
    return front_half + ''.join([str(abs(i) % 10) for i in back_half])

def fft(signal, times):
    base = [0, 1, 0, -1]
    pattern_matrix = generate_pattern_matrix(base, len(signal))[:int(len(signal)/2)]
    for i in range(times):
        signal = fft_once(signal, pattern_matrix)
    return signal

def backwards_cumsum(x):
    return np.cumsum(x[::-1])[::-1]

assert fft('12345678', 1) == '48226158'
assert fft('12345678', 2) == '34040438'
assert fft('12345678', 3) == '03415518'
assert fft('12345678', 4) == '01029498'

assert fft('80871224585914546619083218645595', 100)[:8] == '24176176'

input = read_input('day16.txt')[0]
output = fft(input, 100)
assert output[:8] == '22122816'
