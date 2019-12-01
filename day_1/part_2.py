from day_1 import fuel_calculator
import sys


def solve_part_2():
    fuel_needed = 0
    with open(sys.path[0] + '/day_1/input.txt', 'r') as f:
        for line in f:
            fuel_needed += fuel_calculator.count_fuel_needed(int(line), 0, True)

    return fuel_needed
