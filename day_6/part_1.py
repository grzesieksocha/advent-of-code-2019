from day_6.orbiter import count_orbits
import sys


def solve_part_1():
    with open(sys.path[0] + '/day_6/input.txt') as file:
        orbits = [line.rstrip('\n') for line in file]

    return count_orbits(orbits)[0]
