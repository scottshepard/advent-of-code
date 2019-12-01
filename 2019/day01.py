from math import floor
import numpy as np
import advent_of_code as aoc


def calculate_fuel(mass):
    mass = int(mass)
    fuel = floor(mass / 3.0) - 2
    if fuel < 0:
        fuel = 0
    return fuel


def fuel_for_fuel(fuel_mass):
    f = calculate_fuel(fuel_mass)
    total = f
    while f > 0:
        f = calculate_fuel(f)
        total += f
    return total


def solve01(input_):
    return np.array([calculate_fuel(mass) for mass in input_]).sum()


def solve02(input_):
    base_fuel = [calculate_fuel(mass) for mass in input_]
    return np.array([bf + fuel_for_fuel(bf) for bf in base_fuel]).sum()


if __name__ == '__main__':
    input = aoc.read_input('day01.txt')
    print('Answer to part 1 is {}'.format(solve01(input)))
    print('Answer to part 2 is {}'.format(solve02(input)))
