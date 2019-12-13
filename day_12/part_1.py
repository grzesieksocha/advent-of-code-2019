from day_12.planet import Planet
import sys
from itertools import combinations
from functools import reduce
from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def create_planet(positions: str):
    return Planet(list(map(lambda position: int(position[position.find('=') + 1:]), positions.split(','))))


def count_pair_velocity(planet_one: Planet, planet_two: Planet):
    for coord in range(3):
        if planet_one.position[coord] > planet_two.position[coord]:
            planet_two.velocity[coord] += 1
            planet_one.velocity[coord] -= 1
        elif planet_two.position[coord] > planet_one.position[coord]:
            planet_two.velocity[coord] -= 1
            planet_one.velocity[coord] += 1


def define_velocities(planets: list):
    for pair in combinations([0, 1, 2, 3], 2):
        count_pair_velocity(planets[pair[0]], planets[pair[1]])


def move(planets: list):
    for planet in planets:
        for key, velocity in enumerate(planet.velocity):
            planet.position[key] += velocity


def solve_part_1():
    planets = []
    with open(sys.path[0] + '/day_12/input.txt', 'r') as f:
        for line in f:
            planets.append(create_planet(line.rstrip('>\n')))

    for _ in range(1000):
        define_velocities(planets)
        move(planets)

    print(sum(map(lambda planet: planet.get_total_energy(), planets)))


def solve_part_2():
    planets = []
    with open(sys.path[0] + '/day_12/input.txt', 'r') as f:
        for line in f:
            planets.append(create_planet(line.rstrip('>\n')))

    number_of_steps = 0

    '''
    orbital_periods {0: x aligned, 1: y aligned, 2: z aligned}
    '''
    period = dict()

    initial_position = [[(planet.position[coord], planet.velocity[coord]) for planet in planets] for coord in range(3)]

    while len(period) < 3:
        number_of_steps += 1
        define_velocities(planets)
        move(planets)

        for coord in range(3):
            '''
            See if current (pos_axis, vel_axis) for all moons match their starting values:
            '''
            if coord not in period and initial_position[coord] == [(planet.position[coord], planet.velocity[coord]) for
                                                                   planet in planets]:
                period[coord] = number_of_steps

    print(f'After {number_of_steps} steps:')
    print('ans:', reduce(lcm, period.values()))
