from intcode.computer import analyze
import sys


def solve_part_1():
    intcode = list(map(int, open(sys.path[0] + '/day_13/input.txt').read().split(sep=',')))

    extra_memory = [0] * 1000
    intcode += extra_memory

    intcode[0] = 2
    instruction_pointer = 0
    relative_base = 0
    finished = False
    input_type = 0
    x = 0
    y = 0
    tiles = dict()

    while not finished:
        output, instruction_pointer, relative_base, finished = \
            analyze(instruction_pointer, relative_base, intcode, True, [])

        if input_type == 0:
            x = output
            input_type += 1
        elif input_type == 1:
            y = output
            input_type += 1
        elif input_type == 2:
            tiles[(x, y)] = output
            input_type = 0

    count_blocks = 0
    for tile in tiles.values():
        print(tile)
        if tile == 2:
            count_blocks += 1

    print(count_blocks)
