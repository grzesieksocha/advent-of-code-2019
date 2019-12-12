from intcode.computer import analyze
import sys


def paint(path: list, color: int, colors: dict):
    hull_to_paint = path[len(path) - 1]
    colors[hull_to_paint] = color


def move(path: list, previous_move_direction: tuple, direction: int):
    direction_changer = 1
    if direction == 0:
        direction_changer = -1

    if previous_move_direction == (0, 1):
        direction = (direction_changer * 1, 0)
    elif previous_move_direction == (-1, 0):
        direction = (0, direction_changer * 1)
    elif previous_move_direction == (0, -1):
        direction = (direction_changer * -1, 0)
    elif previous_move_direction == (1, 0):
        direction = (0, direction_changer * -1)

    last_field = path[len(path) - 1]
    path.append((last_field[0] + direction[0], last_field[1] + direction[1]))

    return direction


def solve_part_1(first_hull_color: int):
    intcode = list(map(int, open(sys.path[0] + '/day_11/input.txt').read().split(sep=',')))
    extra_memory = [0] * 1000
    intcode += extra_memory
    instruction_pointer = 0
    relative_base = 0
    finished = False
    path = [(0, 0)]
    colors = {(0, 0): first_hull_color}
    computer_input = [first_hull_color]
    previous_move_direction = (0, 1)
    paint_output = 1

    while not finished:
        output, instruction_pointer, relative_base, finished = \
            analyze(instruction_pointer, relative_base, intcode, True, computer_input)
        if not finished and paint_output:
            paint(path, output, colors)
            paint_output = 0
        elif not finished:
            previous_move_direction = move(path, previous_move_direction, output)
            if path[len(path) - 1] in colors.keys():
                computer_input = [colors[path[len(path) - 1]]]
            else:
                computer_input = [0]
            paint_output = 1

    return colors
