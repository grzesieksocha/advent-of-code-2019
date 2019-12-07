from day_6.part_1 import solve_part_1
from day_6.class_solution import solve_class_part_1


def main():
    part_1_solution = solve_part_1()
    print(f'day 6 - part 1: {part_1_solution}')

    all_planets = solve_class_part_1()
    my_planet = all_planets['YOU']
    santa_planet = all_planets['SAN']

    planet = my_planet
    my_orbits_path = []
    while planet.is_orbiting:
        my_orbits_path.append(planet.name)
        planet = planet.is_orbiting

    planet = santa_planet
    santa_orbits_path = []
    while planet.is_orbiting:
        santa_orbits_path.append(planet.name)
        planet = planet.is_orbiting

    for my_key, planet_in_path in enumerate(my_orbits_path):
        if planet_in_path in santa_orbits_path:
            santa_key = santa_orbits_path.index(planet_in_path)
            print(
                f'Planet {planet_in_path} is {my_key - 1} steps from me and '
                f'{santa_key - 1} from him! {my_key + santa_key - 2} is the answer')
            break


main()
