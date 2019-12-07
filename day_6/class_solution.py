from sys import path


class Planet:
    def __init__(self, name):
        self.name = name
        self.is_orbiting = None

    def orbits(self, planet):
        self.is_orbiting = planet


def solve_class_part_1():
    with open(path[0] + '/day_6/input.txt') as file:
        orbits = [line.rstrip('\n') for line in file]

    planets = {}
    for pair in orbits:
        orbited, orbiting = pair.split(')')
        if orbited not in planets.keys():
            planets[orbited] = Planet(orbited)

        if orbiting not in planets.keys():
            planets[orbiting] = Planet(orbiting)

        planets[orbiting].orbits(planets[orbited])

    return planets
