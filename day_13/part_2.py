from intcode.computer import analyze
import sys


def solve_part_2():
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
    movement = []
    ball_x = 0
    paddle_x = 0

    while not finished:
        output, instruction_pointer, relative_base, finished = \
            analyze(instruction_pointer, relative_base, intcode, True, movement)

        if input_type == 0:
            x = output
        elif input_type == 1:
            y = output
        elif x == -1 and y == 0:
            print(f'Score: {output}')
        elif output == 4:
            ball_x = x
            tiles[(x, y)] = output
        elif output == 3:
            paddle_x = x
            tiles[(x, y)] = output
        else:
            tiles[(x, y)] = output

        input_type = (input_type + 1) % 3
        movement = define_move(ball_x, paddle_x)


def define_move(ball_x, paddle_x):
    if ball_x == paddle_x:
        movement = 0
    elif ball_x > paddle_x:
        movement = 1
    else:
        movement = -1

    return [movement]
