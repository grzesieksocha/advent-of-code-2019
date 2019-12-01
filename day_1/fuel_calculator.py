from math import floor


def count_fuel_needed(mass, initial_value=0, include_fuel_mass=False):
    fuel_for_mass = (floor(mass / 3)) - 2
    if not include_fuel_mass:
        return initial_value + fuel_for_mass

    if fuel_for_mass <= 0:
        return initial_value
    else:
        total = initial_value + fuel_for_mass
        return count_fuel_needed(fuel_for_mass, total, True)
