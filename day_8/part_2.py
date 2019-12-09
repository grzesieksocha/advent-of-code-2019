from day_8.part_1 import solve_part_1
from textwrap import wrap


def solve_part_2():
    layers = solve_part_1()[1]
    picture = [2] * 150

    for layer in layers:
        for pos, digit in enumerate(layer):
            digit = int(digit)
            if digit != 2 and picture[pos] == 2:
                picture[pos] = digit

    picture = ''.join(str(digit) for digit in picture)
    rows = wrap(picture, 25)
    for row in rows:
        print(' '.join(str(digit) for digit in row))
