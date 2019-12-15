import sys
from copy import deepcopy


def resolve(element: list, reactions: dict, leftovers: dict):
    quantity_needed = int(element[0])
    element = element[1]
    quantity_produced = 0
    increment = 0

    quantity_made_in_reaction = int(reactions[element][0][0])
    while quantity_produced < quantity_needed:
        increment += 1
        quantity_produced += quantity_made_in_reaction

    elements_needed = deepcopy(reactions[element][1])
    for pair in elements_needed:
        pair[0] = int(pair[0]) * increment

    if element in leftovers.keys():
        leftovers[element] += quantity_produced - quantity_needed
    else:
        leftovers[element] = quantity_produced - quantity_needed

    return elements_needed


def consolidate_and_use_leftovers(for_fuel, leftovers):
    new_for_fuel = []
    temp_dict = dict()
    for element in for_fuel:
        if element[1] in temp_dict.keys():
            temp_dict[element[1]] += int(element[0])
        else:
            temp_dict[element[1]] = int(element[0])

    for key in temp_dict.keys():
        if key in leftovers.keys():
            if temp_dict[key] >= leftovers[key]:
                new_for_fuel.append([temp_dict[key] - leftovers[key], key])
                leftovers[key] = 0
            else:
                leftovers[key] = leftovers[key] - temp_dict[key]
        else:
            new_for_fuel.append([temp_dict[key], key])

    return new_for_fuel


def solve_part_1():
    reactions = dict()
    with open(sys.path[0] + '/day_14/input.txt', 'r') as f:
        for line in f:
            data = list(map(lambda formula: formula.strip(), line.rstrip('\n').split('=>')))
            product = data[1].split()
            reactions[product[1]] = [list(product), list(
                map(lambda formula: list(formula.strip().split()), data[0].split(',')))]

    leftovers = dict()
    result = []
    for_fuel = reactions['FUEL'][1]
    while for_fuel:
        for_fuel = resolve(for_fuel[0], reactions, leftovers) + for_fuel[1:]
        if for_fuel[0][1] == 'ORE':
            result.append(for_fuel.pop(0))

        for_fuel = consolidate_and_use_leftovers(for_fuel, leftovers)

    ore_needed = 0
    for needed in result:
        ore_needed += needed[0]

    print(ore_needed)
