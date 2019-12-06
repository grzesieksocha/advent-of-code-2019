from day_6.orbiter import count_orbits
import sys


def solve_part_2():
    with open(sys.path[0] + '/day_6/input.txt') as file:
        orbits = [line.rstrip('\n') for line in file]

    orbits_map = count_orbits(orbits)[1]
    my_orbited = orbits_map['YOU']
    santa_orbited = orbits_map['SAN']

    for my_orb in my_orbited:
        if my_orb in santa_orbited:
            print(my_orb)

    return 'Good luck ;)'
