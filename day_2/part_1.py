from intcode.computer import analyze
import sys


def solve_part_1():
    intcode = list(map(int, open(sys.path[0] + '/day_2/input.txt').read().split(sep=',')))
    intcode[1] = 12
    intcode[2] = 2
    return analyze(0, intcode)[2][0]
