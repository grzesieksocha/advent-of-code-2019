import sys
from textwrap import wrap


def solve_part_1():
    intcode = open(sys.path[0] + '/day_8/input.txt').readline()
    layers = wrap(intcode, 150)

    layer_data = []
    for layer in layers:
        zeros = 0
        ones = 0
        twos = 0
        for digit in layer:
            if int(digit) == 0:
                zeros += 1
            elif int(digit) == 1:
                ones += 1
            elif int(digit) == 2:
                twos += 1
        layer_data.append([zeros, ones, twos])

    layer_with_fewest_zeros = 0
    zeros = layer_data[0][0]
    for key, layer in enumerate(layer_data):
        if layer[0] < zeros:
            layer_with_fewest_zeros = key
            zeros = layer[0]

    return layer_data[layer_with_fewest_zeros][1] * layer_data[layer_with_fewest_zeros][2], layers
