import sys
from copy import deepcopy


def resolve(element: list, reactions: dict, leftovers: dict):
    quantity_needed = int(element[0])
    element = element[1]
    quantity_produced = 0
    increment = 0

    quantity_made_in_reaction = int(reactions[element][0][0])
    print(quantity_needed)
    print(quantity_made_in_reaction)
    print(leftovers)
    if element in leftovers.keys() and quantity_needed % quantity_made_in_reaction < leftovers[element]:
        quantity_needed -= quantity_needed % quantity_made_in_reaction
        leftovers[element] -= quantity_needed % quantity_made_in_reaction
    if element in leftovers.keys() and quantity_needed < leftovers[element]:
        leftovers[element] -= quantity_needed
        return []
    else:
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


def solve_part_1():
    reactions = dict()
    with open(sys.path[0] + '/day_14/test_data/test_3.txt', 'r') as f:
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

    ore_needed = 0
    for needed in result:
        ore_needed += needed[0]

    print(ore_needed)
